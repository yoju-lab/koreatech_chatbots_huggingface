from fastapi import FastAPI

app = FastAPI()

# http://localhost:8000/items/1
@app.get("/items/{item_id}")
def read_item(item_id: str):
  return {"item_id": item_id}

# http://localhost:8000/friend/둘리/10
@app.get("/friend/{name}/{age}")
async def read_item(name: str, age: int):
  return {"이름": name, "나이" : age}