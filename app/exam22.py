from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form
from transformers import pipeline
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import os

ml_model = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Load the ML model
  ml_model["translation"] = pipeline("translation", model="Helsinki-NLP/opus-mt-ko-en")
  ml_model["classifier"] = pipeline("sentiment-analysis")
  yield
  # Clean up the ML models and release the resources
  ml_model.clear()

app = FastAPI(lifespan=lifespan)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.post("/predict", response_class = HTMLResponse)
def predict(content: Annotated[str, Form()]):
  print(content)
  translated_text = ml_model["translation"](content)
  eng_content = translated_text[0]['translation_text']
  print(eng_content)
  result = ml_model["classifier"](eng_content)
  
  return f"<h3>{result[0]['score']:.3f}% 정확도로 {'긍정' if result[0]['label'] == 'POSITIVE' else '부정'}입니다.</h3>"

@app.get("/")
async def main():
  content = """
      <!DOCTYPE html> 
      <html>
        <head>
        <meta charset="UTF-8">
        <title>HTML학습</title>
      </head>
      <body>
        <h1>Hugging Face AI Model 활용</h1>
        <img src="static/images/hf1.png" width="100">
        <hr>
        <h3>긍정&부정을 채크하려는 문장을 한국어로 입력하세요.</h3>
        <form action="/predict" method="post">
					<textarea name="content" rows="5" cols="50"></textarea><br>
					<input type="submit" value="요청">
        </form>
      </body>
    """
  return HTMLResponse(content=content)