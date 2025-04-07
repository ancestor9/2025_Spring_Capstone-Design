## 📌 LangChain의 핵심 개념 요약
##### LangChain은 LLM(대형 언어 모델, 예: ChatGPT, Claude 등)을 활용한 애플리케이션을 쉽게 만들 수 있도록 지원하는 파이썬 기반 프레임워크
##### 언어 모델을 단순히 호출하는 데서 그치지 않고, 다양한 외부 도구 및 데이터와 결합해 복잡한 기능을 구현할 수 있게 해주는 구조를 제공

| 개념              | 설명                                                                 |
|-------------------|----------------------------------------------------------------------|
| **LLM**           | GPT-4, Claude, Cohere 같은 대형 언어 모델을 의미                     |
| **Prompt Templates** | 재사용 가능한 프롬프트 틀. 사용자 입력을 템플릿에 자동 삽입         |
| **Chains**        | 여러 컴포넌트를 순차적으로 연결해 하나의 플로우 구성<br>(예: 프롬프트 → LLM → 결과 후처리) |
| **Agents**        | LLM이 툴(검색, 계산기, 코드 실행 등)을 **스스로 선택**해서 문제 해결 |
| **Tools**         | LLM이 사용할 수 있는 외부 도구 (예: Google 검색, Pandas, API 호출 등) |
| **Memory**        | 대화 이력 기억. 챗봇이 문맥을 유지하도록 해줌                         |
| **Document Loaders** | PDF, 웹페이지, DB 등 다양한 출처에서 문서를 불러옴               |
| **Vector Stores** | 임베딩된 문서를 저장해서 유사한 정보를 검색<br>(RAG 방식에서 필수)    |


1. Tokenizer와 WordEmbedding, Vector DB
2. Chat prompt-template, Chains
3. 외부데이터(pdf, excel, ppt, word emd) 로딩하기

## claude에서 MCP => file system와 brave search
--> https://www.youtube.com/watch?v=Ug1w8Lr4Sy8

1. https://claude.ai/download (claude desktop 다운로드)
2. https://nodejs.org/ko (Node.js 설치)
3. https://github.com/modelcontextprotocol (깃허브 MCP)
