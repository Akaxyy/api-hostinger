from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float

app = FastAPI(title="API Test", version="1.0.0")

@app.get('/')
async def root():
    return {"message": "Hello World!"}

@app.get("/itens")
def list_item():
    return [
        {"id": 1, "name": "Mouse", "price": 99.90},
        {"id": 2, "name": "Teclado", "price": 199.90}
    ]

@app.post("itens")
def create_item(item: Item):
    return {"message": "Item criado com sucesso!", "data": item}

@app.get("/itens/{item_id}")
def find_item(item_id: int):
    return {"id": item_id, "nome": "Item genérico", "preco": 10.0}

