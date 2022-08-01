import os
from fastapi import FastAPI

from bot import start_bot, hello

TOKEN = os.environ["TELEGRAM_API_TOKEN"]

app = FastAPI()


@app.get("/helth", status_code=200)
async def root():
    return {"message": "Ok"}

@app.get("/start", status_code=200)
def starter():
    start_bot()
    return {"message": "Ok"}

@app.get("/hello", status_code=200)
def starter():
    hello()
    return {"message": "Ok"}
