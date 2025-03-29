# MoBi-AI WebChatbot (KoAlpaca 기반 + 장기 기억)

## ✨ 특징
- KoAlpaca 모델 사용 → 한국어 완전 특화
- 사용자 ID 기반으로 대화 히스토리 저장
- 최대 10개까지 기억해서 연속 대화 가능
- FastAPI + HTML/JS 구조로 웹 기반 챗봇 운영 가능

## ✅ 실행 방법

### 백엔드
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
