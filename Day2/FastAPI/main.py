from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
@app.get("/about")
def about():
    return {"message": "This is a FastAPI application."}
@app.get("/usn/{usn}")
def get_usn(usn: str):
    return {"usn": usn}

class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"item": item,"total_price": item.price * 1.1}
