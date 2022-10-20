from tkinter.tix import Tree
from fastapi import FastAPI , status ,  HTTPException , Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import requests

app = FastAPI()
app.mount("/client", StaticFiles(directory="client"), name="client")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8043,reload=True)