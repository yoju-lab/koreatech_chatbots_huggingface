from fastapi import Request

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# http://localhost:8000/calc?num1=2&num2=3
@app.get("/calc")
async def calc(num1: int, num2: int):
    return {"result" : num1 * num2}

# http://localhost:8000/
@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("exam9_v.html",{"request":request})