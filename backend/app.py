from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from koalpaca_caller import call_koalpaca
from memory import update_memory, get_memory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class PromptRequest(BaseModel):
    prompt: str
    user_id: str

@app.post("/generate")
async def generate_text(req: PromptRequest):
    history = get_memory(req.user_id)
    prompt_with_context = history + "\n" + req.prompt
    response = call_koalpaca(prompt_with_context)
    update_memory(req.user_id, req.prompt, response)
    return {"response": response}
