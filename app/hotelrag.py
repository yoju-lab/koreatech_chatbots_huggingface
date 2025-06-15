from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pgvector.psycopg import register_vector
import psycopg
import numpy as np
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import os
from dotenv import load_dotenv

ml_model = {}

# .env 파일 로드
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(env_path)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the AI model
    ml_model["embedding_model"] = SentenceTransformer("upskyy/bge-m3-korean", device="cpu")
    lm_model_name = os.getenv("LM_MODEL_NAME", "gpt2")
    hf_token = os.getenv("HF_TOKEN", None)
    if hf_token:
        ml_model["lm_model"] = pipeline("text-generation", model=lm_model_name, use_auth_token=hf_token)
    else:
        ml_model["lm_model"] = pipeline("text-generation", model=lm_model_name)
    print("AI 모델 로드 완료")
    yield
    ml_model.clear()

app = FastAPI(lifespan=lifespan)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:5501",
    "http://127.0.0.1:5501"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# http://localhost:8000/rag?query=호텔 예약
@app.get("/rag")
async def rag(query : str):
    conn = psycopg.connect(dbname='edudb', user='edu', password='1234'
                        #    , host='localhost', port=5432
                       , host='edupgvector', port=5432
                        , autocommit=True)
    conn.execute('CREATE EXTENSION IF NOT EXISTS vector')
    register_vector(conn)

    input = 'search_query: '+query
    embedding =  ml_model["embedding_model"].encode(input)

    result = conn.execute(
        'SELECT content FROM hotel ORDER BY embedding <=> %s LIMIT 1', (np.array(embedding),)).fetchall()

    context = '\n\n'.join([row[0] for row in result])
    context = context[2:]

    prompt = f'Answer this question: {query}\n\n{context}'

    response = ml_model["lm_model"](prompt)
    print(response)
    return {"message": response}




