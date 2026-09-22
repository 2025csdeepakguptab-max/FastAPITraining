from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["college"]
collection = db["students"]

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI MongoDB example!"}
@app.get("/health")
async def health_check():
    result = db.command("ping")
    return {"MongoDB connection": "successful", "ping": result["ok"]}