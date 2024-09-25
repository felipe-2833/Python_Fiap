from datetime import datetime
from pathlib import Path
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

class Car(BaseModel):
    report_recived_date: str | None
    manufactured: str | None
    component: str | None
    recall_type: str | None
    potentially_affected: int | None


app = FastAPI()

fake_items_db = [
    {"item_name": "Foo", "item_id":1}, 
    {"item_name": "Bar","item_id":2}, 
    {"item_name": "Baz","item_id":3},
    
    ]

db = pd.read_csv(Path(__file__).parent / "bd.csv")

car = {"abacate":"R$100,00",}


@app.get("/cars")
async def root():
    return {
        "message": "Hello world",
        "endpoint": "/cars",
        "description": "API para consulta de dados de recall de veículos",
        "version": "1.0.0",
        "timestamp":  datetime.now().isoformat(),
    }
    

@app.get("/cars/info")
async def read_cars_info():
    return db.describe().to_dict()

@app.get("/cars/info/columns")
async def read_cars_info_columns():
    return db.columns.to_list()

@app.get("/cars/info/columns/{column}")
async def read_cars_info_columns(column:str):
    return db[column].unique.tolist()

@app.get("/cars/info/columns/{column}/")
async def read_cars_info_columns_value(column:str, value:str|float):
    return db[db[column] == value].head().to_dict(orient="records")

@app.get("/cars/")
async def head(start: int=0, stop:int=1):
    return db.iloc[start:stop].to_dict(orient="record")

@app.post("/cars/")
async def create_car(car: Car):
    db.loc[db.shape[0]] = car.model_dump()
    db.to_csv(Path(__file__).parent / "bd.csv", idex=False)
    return{"Status" : "Sucess"}
    
@app.patch("/cars/{column}")
async def update_car(column: str, value:str, car: Car):
    idx = db[column] == value
    if not idx.any():
        return {"status" : "error", "message":"Nenhum registro encontrado"}
    db[idx] = car.model_dump()
    return db[idx].head().to_dict(orient="records")
    

    
    
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     def _get_item_by_id(id: int):
#         for item in fake_items_db:
#             if item.get("item_id") == id:
#                 return item
#         return {"error": "item not found"}
#     return _get_item_by_id(item_id)



