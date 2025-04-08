from agents import Agent, Runner
from dotenv import load_dotenv

# .env 파일 로드 (API 키 등 환경 변수 사용을 위해)
load_dotenv()
def main():
    # LLM 에이전트 구성: 이름, 명령어, 모델 설정
    agent = Agent(
        name='Assistant',
        instructions='You are a helpful assistant. Always maintain memory of the conversation history and remember the user\'s name is Dabid.',
        model="gpt-4o-mini", 
        )
    
    # 사용자와의 대화 기록 저장 리스트
    messages = []
    
    # 무한 루프: 사용자 입력 → LLM 응답 → 반복
    while True:
        user_input = input("\nYou: ")                          # 사용자 입력 받기
        messages.append({"role": "user", "content": user_input}) # 입력을 히스토리에 저장

        print("Assistant: ", end="")
        result = Runner.run_sync(
            agent, 
            input=messages   # 전체 대화 히스토리를 전달
        )

        # LLM 최종 응답 추출 및 출력
        assistant_response = str(result.final_output)
        print(assistant_response)

        # LLM 응답도 히스토리에 저장
        messages.append({"role": "assistant", "content": assistant_response})

# Run it
if __name__ == "__main__":
    main()
