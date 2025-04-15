### https://platform.openai.com/playground/prompts?models=gpt-4.1
- Function을 이해하기
- RAG를 이해하기
  
### https://www.youtube.com/watch?v=Rn5HMaWunx4 
- https://github.com/dabidstudio/python_mcp_agent

# MCP 아키텍처 개요

## 🏗️ 기본 구조

- **클라이언트-서버 아키텍처 기반**
- LLM 애플리케이션과 **외부 데이터 소스/도구 간 통합**을 위한 프레임워크

---

## 🧩 주요 구성 요소

| 구성 요소            | 설명 |
|---------------------|------|
| **호스트 애플리케이션 (MCP 호스트)** | LLM 기반 앱 (예: 채팅 클라이언트, IDE 등) |
| **클라이언트 (MCP 클라이언트)**       | 호스트 앱 내에서 MCP 서버와 **1:1 연결 유지** |
| **서버 (MCP 서버)**                | 표준화된 MCP 프로토콜을 통해 기능 제공<br>로컬 또는 원격 데이터 소스 접근 지원 |

---

## 🔧 핵심 컴포넌트

### 1. **프로토콜 레이어**
- 메시지 프레이밍
- 요청/응답 연결 및 통신 패턴 관리

### 2. **전송 레이어**
- **STDIO 전송**: 로컬 프로세스 간 통신
- **HTTP with SSE 전송**: 서버-클라이언트 및 클라이언트-서버 간 통신

---

## 💬 메시지 유형

| 메시지 유형   | 설명 |
|--------------|------|
| **요청 (Requests)**    | 응답을 기대하는 작업 시작 |
| **결과 (Results)**     | 요청에 대한 **성공 응답** |
| **오류 (Errors)**      | 요청 실패를 나타냄 |
| **알림 (Notifications)** | 응답을 기대하지 않는 **단방향 메시지** |

---

## 🔄 연결 생명주기

1. **초기화**
   - 클라이언트 → 서버: 프로토콜 버전 및 기능 전송
   - 서버 → 클라이언트: 응답
   - 클라이언트 → 서버: 확인

2. **메시지 교환**
   - 요청-응답 상호작용
   - 필요에 따라 알림 전송

3. **종료**
   - 정상 종료
   - 연결 해제
   - 오류로 인한 종료

---

## 🎯 설계 목표

- **모듈화 및 확장성 확보**
- LLM 애플리케이션과 다양한 도구/데이터 소스 간 **유연한 통합 지원**


###  실습파일 작동 매커니즘

| 단계 | 설명 | 관련 Python 파일 | 주요 역할 |
|------|------|------------------|------------|
| 1 | 사용자 질문 입력 | `4_mcp_client.py` | Streamlit UI에서 사용자가 질문 입력 (`st.chat_input`) |
| 2 | 질문 메시지 세션에 저장 | `4_mcp_client.py` | `st.session_state.chat_history`에 사용자 메시지 추가 |
| 3 | MCP 서버 연결 설정 | `4_mcp_client.py`<br>`mcp.json` | `setup_mcp_servers()` 함수가 `mcp.json`의 명령어로 MCP 서버 실행 및 연결 |
| 4 | LLM 기반 Agent 초기화 | `4_mcp_client.py` | `Agent(...)` 객체에 `mcp_servers` 포함하여 생성됨 |
| 5 | 사용자 메시지를 LLM에 전달 | `4_mcp_client.py` | `Runner.run_streamed()` 호출로 대화 히스토리를 GPT-4o-mini에 입력 |
| 6 | LLM이 MCP Tool 호출 필요 판단 | `4_mcp_client.py` 내부<br>(자동 처리) | 메시지 중 일부를 처리하기 위해 MCP 서버의 툴 함수 호출 결정 |
| 7 | MCP 서버로 Tool 요청 전송 | `4_mcp_client.py`<br>↔ `2_mcp_server.py` | MCPServerStdio 통해 `get_youtube_transcript`, `search_youtube_videos` 등 호출 |
| 8 | MCP 서버에서 도구 실행 | `2_mcp_server.py` | 등록된 `@mcp.tool()` 함수가 호출되어 유튜브 API 처리 |
| 9 | Tool 실행 결과 LLM에 전달 | `4_mcp_client.py` 내부 처리 | Tool 출력 결과가 다시 GPT 모델로 돌아가 응답 생성 재료로 사용됨 |
| 10 | 최종 응답 생성 | `4_mcp_client.py` | GPT-4o-mini가 Tool 결과를 바탕으로 자연어 응답 생성 |
| 11 | 실시간 스트리밍 출력 | `4_mcp_client.py` | `async for event in result.stream_events()` 통해 실시간으로 응답 토큰 출력 |
| 12 | 사용자 화면에 출력 | `4_mcp_client.py` + Streamlit | `st.chat_message()`로 LLM 응답이 사용자에게 출력됨 |
