from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from koalpaca_caller import call_koalpaca
from memory import update_memory, get_memory

# FastAPI 앱 초기화
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 프론트엔드 URL로 제한 가능
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 루트 경로 (서버 정상 작동 확인용)
@app.get("/")
def root():
    return {"message": "MoBi-AI 서버 정상 작동 중!"}

# 프롬프트 요청 모델 정의
class PromptRequest(BaseModel):
    prompt: str
    user_id: str

# ✅ 생성 API
@app.post("/generate")
async def generate_text(req: PromptRequest):
    history = get_memory(req.user_id)
    prompt_with_context = history + "\n" + req.prompt
    response = call_koalpaca(prompt_with_context)
    update_memory(req.user_id, req.prompt, response)
    return {"response": response}
