from fastapi import FastAPI

app = FastAPI()

# http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "안녕? FastAPI!! ^^"}




