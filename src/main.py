import os 
from fastapi import FastAPI
from src.env import config

#MODE = os.environ.get("MODE") or "dev"
MODE = config("MODE", cast = str, default = "testing")

app = FastAPI()

@app.get("/")
def home_page():
    return {"Hello": "World", "mode": MODE}

