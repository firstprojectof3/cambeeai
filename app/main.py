
# FAST API AI 앱 실행, 라우팅 처리
from fastapi import FastAPI
from app.models.chat import ChatRequest, ChatResponse
from openai import OpenAI 
from datetime import datetime 

from app.services.ai.prompt.prompt_builder import build_generic_prompt
from app.models.user_db import get_user_by_id
from app.services.ai.ai_setting import call_openai

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    user = get_user_by_id(req.user_id)
    prompt = build_generic_prompt(user, req.message)
    
    response = call_openai(client, [
        {"role": "system", "content": prompt},
        {"role": "user", "content": req.message}
    ])
    
    if not response or not response.choices:
        return ChatResponse(
        summary="AI 응답을 가져오지 못했습니다.",
        timestamp=datetime.now().isoformat()
    )

    return ChatResponse(
    summary=response.choices[0].message.content,
    timestamp=datetime.now().isoformat()
    
)


