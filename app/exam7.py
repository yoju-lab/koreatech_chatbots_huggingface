from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

templates = Jinja2Templates(directory="templates")

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get("/html1")
async def test1(request: Request):
    return templates.TemplateResponse("exam7_1.html",{"request":request})

@app.get("/html2") 
async def test2(request: Request):
    return templates.TemplateResponse("exam7_2.html",{"request":request})