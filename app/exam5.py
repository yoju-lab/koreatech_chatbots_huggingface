from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Dooly"}, {"item_name": "Ddochi"}, {"item_name": "Dauner"}, {"item_name": "Olaf"}]

# http://localhost:8000/items?skip=0&limit=10
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
  return fake_items_db[skip : skip + limit]

# http://localhost:8000/items/1?q=fastapi
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
  if q:
    return {"item_id": item_id, "q": q}
  return {"item_id": item_id}