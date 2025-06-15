from fastapi import FastAPI

app = FastAPI()

# http://localhost:8000/test1
@app.get("/test1")
async def root1():
  return {"name": "둘리"}

# http://localhost:8000/test2
@app.get("/test2")
async def root2():
  return ["둘리", "또치", "도우너"]

# http://localhost:8000/test3
@app.get("/test3")
async def root3():
  return "<h1>안녕?</h1>"

# http://localhost:8000/test4
@app.get("/test4")
async def root4():
  return 1000