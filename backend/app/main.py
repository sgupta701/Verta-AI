# backend/app/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.translator import Translator
from app.utils.language_utils import get_model_config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()

@app.get("/")
def read_root():
    return {"message": "Lingua.ai backend is running"}

@app.post("/translate")
async def translate(request: Request):
    data = await request.json()
    src_text = data["text"]
    src_lang = data["src_lang"]
    tgt_lang = data["tgt_lang"]

    model_config = get_model_config(src_lang, tgt_lang)
    if not model_config:
        return {"error": "Unsupported language pair"}

    model_name = model_config["model"]
    src_code = model_config["src_lang"]
    tgt_code = model_config["tgt_lang"]

    result = translator.translate(src_text, model_name, src_lang=src_code, tgt_lang=tgt_code)
    return {"translated_text": result}
