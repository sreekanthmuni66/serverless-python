from fastapi import FastAPI

MODE = "dev"

app = FastAPI()

@app.get("/")
def home_page():
    return {"Hello": "World", "mode": MODE}

