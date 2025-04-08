import sys
import asyncio
import streamlit as st
import json
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner # LLM 에이전트 실행
from agents.mcp import MCPServerStdio # MCP 서버와 터미널 통해 통신
from dotenv import load_dotenv

# 환경 변수 로드 (.env에서 API 키 등)
load_dotenv()

# Streamlit UI로 사용자 입력을 받아, LLM + MCP Tool을 조합해 응답을 생성하고 실시간으로 출력하는 에이전트 클라이언트

# Windows 환경에서 asyncio 오류 방지를 위한 설정
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    

# ----------------------------
#  🧠 MCP 서버 연결 설정 함수
# ----------------------------
async def setup_mcp_servers():
    servers = []
    
    # mcp.json 파일에서 설정내용 읽기
    with open('mcp.json', 'r') as f:
        config = json.load(f)
    
    # # 서버 이름과 명령어로 MCP 서버 인스턴스 실행 및 연결, MCP 서버들을 순회
    # 각 MCP 서버를 MCPServerStdio 인스턴스로 감싸고 연결
    # 여러 서버를 동시에 등록할 수도 있음
    for server_name, server_config in config.get('mcpServers', {}).items():
        mcp_server = MCPServerStdio(
            params={
                "command": server_config.get("command"),
                "args": server_config.get("args", [])
            },
            cache_tools_list=True
        )
        await mcp_server.connect()
        servers.append(mcp_server)

    return servers

# --------------------------------------
#  🤖 LLM기반 에이전트 초기화, 설정
# --------------------------------------
async def setup_agent():
    # 서버가 이미 존재하는지 확인하고, 없으면 생성
    mcp_servers = await setup_mcp_servers()
    
    # GPT 모델 + MCP 서버 도구를 연결한 에이전트 생성
    agent = Agent(
        name="Assistant",
        instructions="너는 유튜브 컨텐츠 분석을 도와주는 에이전트야",
        model="gpt-4o-mini",
        mcp_servers=mcp_servers    # LLM + MCP 툴을 모두 사용
    )
    return agent,mcp_servers

# --------------------------------------------------
# 📬 사용자 메시지 처리 + 스트리밍 : 응답메시지 처리
# --------------------------------------------------
async def process_user_message():
    agent,mcp_servers = await setup_agent()
    messages = st.session_state.chat_history # 대화 히스토리 관리
    
    # 메시지를 GPT에 스트리밍 방식으로 전달
    result = Runner.run_streamed(agent, input=messages) 

    response_text = ""
    placeholder = st.empty()
    
    # 스트리밍 응답 출력 처리
    async for event in result.stream_events(): # 스트리밍 토큰 출력 (result.stream_events())
        # LLM 응답 토큰 스트리밍
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            response_text += event.data.delta or ""
            with placeholder.container():
                with st.chat_message("assistant"):
                    st.markdown(response_text)


        # MCP 도구 이벤트와 메시지 완료 처리
        elif event.type == "run_item_stream_event":
            item = event.item

            if item.type == "tool_call_item":
                tool_name = item.raw_item.name
                st.toast(f"🛠 도구 활용: `{tool_name}`")
                
    # 응답을 세션 히스토리에 저장
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response_text
    })
    
    # 명시적 종료 (streamlit에서 비동기 처리 오류 방지)
    for server in mcp_servers:
        await server.__aexit__(None, None, None)

# ----------------------------
# Streamlit UI 메인
# ----------------------------
def main():
    st.set_page_config(page_title="유튜브 에이전트", page_icon="🎥")
    
    # 세션 상태에 대화 기록이 없으면 초기화
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.title("🎥 유튜브 컨텐츠 에이전트")
    st.caption("유튜브 컨텐츠 제작, 아이디어, 트렌드에 대해 물어보세요!")

    for m in st.session_state.chat_history:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # 사용자 입력 처리
    user_input = st.chat_input("대화를 해주세요")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # 비동기 응답 처리
        asyncio.run(process_user_message())
        
# ----------------------------
# 앱 실행
# ----------------------------
if __name__ == "__main__":
    main()
