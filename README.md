# FastAPI Study 🦊

FastAPI를 학습하면서 하나씩 기능을 구현해보는 개인 프로젝트입니다.  
현재는 **회원가입 및 이메일 인증** 기능이 완료되었으며, 이후 인증/인가, CRUD, 사용자 관리, JWT 로그인 등도 순차적으로 추가할 계획입니다.

---

## 📌 현재 구현된 기능

### ✅ 회원가입
- 이메일과 비밀번호를 입력해 계정을 생성할 수 있습니다.
- 중복 이메일 검증 및 기본 유효성 체크가 포함되어 있습니다.

### ✅ 이메일 인증
- 회원가입 시 등록한 이메일로 인증 메일이 발송됩니다.
- 인증 링크 클릭 시 사용자의 이메일이 인증 완료됩니다.
- 인증된 사용자만 주요 기능을 사용할 수 있도록 제한 예정입니다.

---

## 🧰 기술 스택

| 구분         | 기술명                  |
|--------------|--------------------------|
| Language     | Python 3.10+             |
| Framework    | FastAPI                  |
| ASGI Server  | Uvicorn                  |
| DB           | SQLite (개발용)          |
| Email        | FastAPI-Mail / SMTP      |
| Others       | Pydantic, SQLAlchemy, python-dotenv, JWT |

---

## 🗂️ 프로젝트 구조

```bash
fastapi-study/
├── server/
│   ├── api/           # 라우터 (회원가입, 인증 등)
│   ├── core/          # 설정 및 의존성 관리
│   ├── crud/          # DB 접근 로직
│   ├── db/            # DB 연결 및 초기화
│   ├── models/        # SQLAlchemy 모델 정의
│   ├── schemas/       # Pydantic 스키마
│   ├── services/      # 이메일 발송 등 비즈니스 로직
│   └── main.py        # FastAPI 앱 엔트리포인트
├── .gitignore
├── README.md
├── requirements.txt
```

---

## 🚀 실행 방법

```bash
# 1. 가상환경 생성 및 실행
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 의존성 설치
pip install -r requirements.txt

# 3. 서버 실행
uvicorn server.main:app --reload
```

---

## 🔐 환경 변수 (.env 예시)

이 프로젝트는 `.env` 파일을 사용합니다. 루트 디렉토리에 `.env` 파일을 생성하고 아래 내용을 참고해 주세요:

```env
# JWT 설정
SECRET_KEY=fastapi_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Gmail SMTP 설정
EMAIL_SENDER=
EMAIL_PASSWORD=
```

> ⚠️ 실제 이메일 계정 및 비밀번호는 절대 공개 저장소에 업로드하지 마세요.  
> Gmail을 사용하는 경우 [앱 비밀번호](https://support.google.com/accounts/answer/185833?hl=ko)를 발급받아 사용해야 합니다.

---

## 📅 개발 계획

- [x] 회원가입
- [x] 이메일 인증
- [ ] 로그인 / JWT 토큰
- [ ] 마이페이지 조회
- [ ] 비밀번호 재설정
- [ ] 관리자 페이지

---

## 👨‍💻 개발자

- GitHub: [MarvinBaek](https://github.com/MarvinBaek)

---

## 📄 라이선스

MIT License
