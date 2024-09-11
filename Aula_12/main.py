from datetime import datetime
from pathlib import Path
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo", "item_id":1}, 
    {"item_name": "Bar","item_id":2}, 
    {"item_name": "Baz","item_id":3},
    
    ]

db = pd.read_csv(Path(__file__).parent / "bd.csv")

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

    
    
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     def _get_item_by_id(id: int):
#         for item in fake_items_db:
#             if item.get("item_id") == id:
#                 return item
#         return {"error": "item not found"}
#     return _get_item_by_id(item_id)



