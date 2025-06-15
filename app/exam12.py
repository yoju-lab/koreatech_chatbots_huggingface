from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

# http://localhost:8000/items1/?q=hello
@app.get("/items1/")
async def read_items1(q: Union[str, None] = None):
  results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q": q})
  return results

# http://localhost:8000/items2/?q=abcdef
@app.get("/items2/")
async def read_items2(q: Union[str, None] = Query(default=None, min_length=5, max_length=50)):
  results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q": q})
  return results


# http://localhost:8000/items3/?q=unico123
@app.get("/items3/")
async def read_items3(q: Union[str, None] = Query(default=None, min_length=3, max_length=10, pattern="^unico")):
  results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q": q})
  return results

