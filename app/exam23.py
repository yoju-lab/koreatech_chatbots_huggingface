from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
from transformers import pipeline
from contextlib import asynccontextmanager

ml_model = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
	# Load the ML model
	ml_model["summarizer"] = pipeline("summarization", "sshleifer/distilbart-cnn-12-6")
	yield
	# Clean up the ML models and release the resources
	ml_model.clear()


app = FastAPI(lifespan=lifespan)

# http://localhost:8000/summarize (POST)
@app.post("/summarize", response_model = str)
async def summary(file: UploadFile):
	content = await file.read()
	content = content.decode()
	content = content.replace('\r\n', '')
	result = ml_model["summarizer"](content)
	return f"요약된 내용 : {result[0]['summary_text']}"

# http://localhost:8000/
@app.get("/")
async def main():
  content = """
      <body>
        <h2>요약하려는 텍스트 파일을 업로드하세요</h2>
        <hr>
        <form action="/summarize" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
        </form>       
      </body>
    """
  return HTMLResponse(content=content)
