from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# MongoDB-Verbindung
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client["data_warehouse"]
collection = db["warehouse_data"]

# Produktdatenmodell
class Product(BaseModel):
    productID: str
    productName: str
    productQuantity: int

# Lagerhausdatenmodell
class WarehouseData(BaseModel):
    warehouseID: str
    warehouseName: str
    timestamp: str
    warehousePostalCode: int
    warehouseCity: str
    warehouseCountrz: str
    productData: List[Product]

@app.post("/store")
def store_data(item: WarehouseData):
    try:
        collection.insert_one(item.dict())
        return {"status": "success", "message": "Data stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data")
def get_all_data():
    try:
        data = collection.find()
        json_data = dumps(data)
        return JSONResponse(content=json_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
