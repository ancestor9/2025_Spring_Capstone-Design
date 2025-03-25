1. Request 객체에 대해 이해하고 실습하기
  - FastAPI에서 Request 객체는 클라이언트로부터 들어온 HTTP 요청의 정보를 담고 있는 클라스 객체
  - fastapi.Request를 통해 액세스하여 활용하면 요청의 헤더, 바디, 쿼리 파라미터 등 다양한 정보를 처리
  - resuest_main.py

2. jinjatemplate
  - 🚀 FastAPI에서 templates.TemplateResponse()를 사용할 때는 request 객체를 반드시 전달
     ---> request: Request를 함수의 매개변수로 추가하고, TemplateResponse에 포함하여야 함

- jinja
- ├── main.py                # FastAPI 애플리케이션
- ├── templates/             # Jinja2 템플릿 폴더
- │   ├── index.html         # HTML 템플릿
- │   └── bs4_doc.html       # BeautifulSoup 예제 HTML 파일
- │   └── bootstrap_doc.html # bootstrap  (https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- └── static/                # 정적 파일 폴더
-     ├── style.css          # CSS 파일
-     └── script.js          # JavaScript 파일

## 설명
- 작동원리
1. 사용자가 루트 URL (/)에 접속하면 --> GET 요청을 보냄.
2. FastAPI가 비동기 핸들러 (read_root)를 실행.
3. index.html을 찾아 렌더링하고, request 객체를 템플릿으로 사전형으로 전달.
4. HTML 페이지를 클라이언트에게 반환.

- index.html과 main.py의 연결
    <link rel="stylesheet" href="{{ url_for('static', path='style.css') }}">
    --> Jinja2 템플릿 문법 ({{ url_for(...) }})
        {{ url_for('static', path='style.css') }}
        → url_for() 함수는 FastAPI에서 정적 파일(static 폴더 안의 파일)을 불러올 때 사용
        "static": FastAPI에서 정적 파일을 제공하는 엔드포인트 이름
        path='style.css': static 디렉토리 내에서 style.css 파일을 불러오도록 지정
        FastAPI 서버가 실행 중일 때, url_for('static', path='style.css')는 다음과 변환
          <link rel="stylesheet" href="/static/style.css">
        즉 브라우저는 http://127.0.0.1:8000/static/style.css에서 style.css 파일을 불러와 실행

- index.html에 아래 코드를 body안에 넣고 실행해보라!
    <!-- 현재 요청된 URL 표시 -->
    <p><strong>Current URL:</strong> {{ request.url }}</p>  
    <!-- 클라이언트 정보 -->
    <p><strong>Client IP:</strong> {{ request.client.host }}</p>
    <!-- 요청된 HTTP 메서드 -->
    <p><strong>Request Method:</strong> {{ request.method }}</p>
    <!-- User-Agent 표시 -->
    <p><strong>User-Agent:</strong> {{ request.headers.get('user-agent', 'Unknown') }}</p>

-> http://127.0.0.1:8000/ : 사용자가 접속하는 root에 아래 하단에 이게 표시
    Current URL: http://127.0.0.1:8000/
    Client IP: 127.0.0.1
    Request Method: GET
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0
