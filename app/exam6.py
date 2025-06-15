from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
# http://localhost:8000/static/images/cloud_sun.png

# http://localhost:8000/items/1?q=fastapi&short=true
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    """
    - item_id: 경로 파라미터
    - q: 쿼리 파라미터 (예: /items/1?q=fastapi)
    - short: 쿼리 파라미터 (예: /items/1?short=true)
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "유용하고 잘 만들어진 상품"})
    return item

# http://localhost:8000/items2/1?needy=fastapi
@app.get("/items2/{item_id}")
async def read_user_item(item_id: str, needy: str):
    """
    - item_id: 경로 파라미터
    - needy: 쿼리 파라미터 (예: /items2/1?needy=fastapi)
    """
    item = {"item_id": item_id, "needy": needy}
    return item

# http://localhost:8000/call-example/1?needy=fastapi
@app.get("/call-example/{item_id}")
async def call_example(item_id: str, needy: str):
    # 내부적으로 read_user_item 함수를 직접 호출
    result = await read_user_item(item_id, needy)
    return {"called_result": result}