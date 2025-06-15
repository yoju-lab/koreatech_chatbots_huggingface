from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# http://localhost:8000/html1
@app.get("/html1")
async def test1(request: Request):
    return templates.TemplateResponse("exam7_1.html",{"request":request})

# http://localhost:8000/html2
@app.get("/html2") 
async def test2(request: Request):
    return templates.TemplateResponse("exam7_2.html",{"request":request})

# http://localhost:8000/call-html1
@app.get("/call-html1")
async def call_html1(request: Request):
    # 내부적으로 test1 함수 직접 호출
    return await test1(request)