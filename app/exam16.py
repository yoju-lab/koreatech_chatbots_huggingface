from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

# http://localhost:8000/singlefile (POST)
@app.post("/singlefile")
async def create_file(file: bytes = File()):
  return {"file_size": len(file)}

# http://localhost:8000/singleuploadfile (POST)
@app.post("/singleuploadfile")
async def create_upload_file(file: UploadFile):
  return {"filename": file.filename}

# http://localhost:8000/
@app.get("/")
async def main():
  content = """
      <body>
      <body>
      <h2>단일 파일 업로드</h2>
      <hr>
      <form action="/singlefile" enctype="multipart/form-data" method="post">
      <input name="file" type="file">
      <input type="submit">
      </form>
      <hr>
      <form action="/singleuploadfile" enctype="multipart/form-data" method="post">
      <input name="file" type="file">
      <input type="submit">
      </form>
      </body>
    """
  return HTMLResponse(content=content)