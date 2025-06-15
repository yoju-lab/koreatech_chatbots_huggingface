from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

templates = Jinja2Templates(directory="templates")

# http://localhost:8000/items/1
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse(name="exam8_v.html",   
                    context={"request":request,
                              "id": id, "nextid" : 1 if id == 10 else id+1, "img_name" : f"images/{id}.jpg"})

# http://localhost:8000/call-items/1
@app.get("/call-items/{id}", response_class=HTMLResponse)
async def call_items(request: Request, id: int):
    return await read_item(request, id)