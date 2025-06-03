Autor: **Sebastian Profous**
Version: **03-06-2025**

## Dokumentation der Aufgabe

### Aufgabenstellung
In dieser Aufgabe ging es darum, einen Microservice zu erstellen, der die bereits bekannten Warehous-Daten speichert und abruft. Die Daten werden wie immer über REST Schnittstellen verarbeitet und in einer MongoDB DB gespeichert. Des weiteren habe ich laut dem Tutorial die Anwendung in Python und mit FastAPI geschrieben.

### Datenmodell

```json
`{`  
`warehouseID: '1',`  
`warehouseName: 'Linz Bahnhof',`  
`timestamp: '2022-01-02 01:00:00',`  
`warehousePostalCode: 4010,`  
`warehouseCity: 'Linz',`  
`warehouseCountrz: 'Austria',`  
`productData: [`  
`{ productID: '00-443175', productName: 'Bio Orangensaft Sonne', productQuantity: 2500 },`  
`{ productID: '00-871895', productName: 'Bio Apfelsaft Gold', productQuantity: 3420 },`  
`{ productID: '01-926885', productName: 'Ariel Waschmittel Color', productQuantity: 478 },`  
`]`  
`}`
```

### Code-Doku

#### Rest Interface 
Da ich noch nie ein Rest Interface in Python geschrieben habe hier eine kurze doku

**Post**
```python
@app.post("/store")  
def store_data(item: WarehouseData):  
    try:  
        collection.insert_one(item.dict())  
        return {"status": "success", "message": "Data stored successfully."}  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
```

**Get**
```python
@app.get("/data")  
def get_all_data():  
    try:  
        data = collection.find()  
        json_data = dumps(data)  
        return JSONResponse(content=json_data)  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
```

#### Einbindung des Datenmodell
Hier gebe ich vor was für ein Datenmodell mein Microservice verwenden soll

```python
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
```



### Test-Beispiele

**Post**

```bash
curl -X POST http://localhost:4441/store \
  -H "Content-Type: application/json" \
  -d '{
    "warehouseID": "1",
    "warehouseName": "Linz Bahnhof",
    "timestamp": "2022-01-02 01:00:00",
    "warehousePostalCode": 4010,
    "warehouseCity": "Linz",
    "warehouseCountrz": "Austria",
    "productData": [
      { "productID": "00-443175", "productName": "Bio Orangensaft Sonne", "productQuantity": 2500 },
      { "productID": "00-871895", "productName": "Bio Apfelsaft Gold", "productQuantity": 3420 }
    ]
  }'
```

**Get**

```bash
curl http://localhost:4441/data
```

