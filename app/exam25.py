from typing import Union
from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline
from contextlib import asynccontextmanager
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
import os

ml_model = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Load the ML model
  ml_model["summarizer"] = pipeline("summarization", "sshleifer/distilbart-cnn-12-6")
  yield
  # Clean up the ML models and release the resources
  ml_model.clear()

templates = Jinja2Templates(directory="templates")
app = FastAPI(lifespan=lifespan)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static") 

# http://localhost:8000/
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
  return templates.TemplateResponse("exam25_v1.html", {'request': request})

# http://localhost:8000/summarize (POST)
@app.post("/summarize", response_class=HTMLResponse)
async def summary(request: Request, file: UploadFile):
  content = await file.read()
  content = content.decode()
  content = content.replace('\r\n', '')
  result = ml_model["summarizer"](content)
  summary = f"{result[0]['summary_text']}"
  return templates.TemplateResponse("exam25_v2.html", {"request": request, "summary": summary})

# http://localhost:8000/call-summarize (POST)
@app.post("/call-summarize", response_class=HTMLResponse)
async def call_summarize(request: Request, file: UploadFile):
  return await summary(request, file)
