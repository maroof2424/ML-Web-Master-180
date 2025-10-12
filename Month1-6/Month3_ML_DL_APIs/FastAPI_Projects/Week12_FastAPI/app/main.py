from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics Demo",version="1.0")

class Item(BaseModel):
    name: str
    price: float
    quantity: int

@app.get("/")
def read_root():
    return {"msg":"Hello from FastAPI"}

@app.post("/items/")
def create_item(item: Item):
    total = item.price * item.quantity
    return {
        "Item name":item.name,
        "total_price": total,
        "message":f"Recived item {item.name}"
    }