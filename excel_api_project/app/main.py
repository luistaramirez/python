from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from . import excel_utils

app = FastAPI()

class DataRow(BaseModel):
    values: list

class HeaderRow(BaseModel):
    headers: list

@app.post("/crear_excel")
def crear_excel(headers: HeaderRow):
    if not excel_utils.create_excel(headers.headers):
        raise HTTPException(status_code=400, detail="El archivo ya existe.")
    return {"message": "Archivo Excel creado.", "headers": headers.headers}

@app.post("/insertar")
def insertar_fila(data: DataRow):
    data_len = len(data.values)
    current = excel_utils.get_data()
    if not current:
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    if data_len != len(current[0]):
        raise HTTPException(status_code=400, detail=f"Se requieren {len(current[0])} valores.")
    if not excel_utils.insert_row(data.values):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    return {"message": "Fila insertada.", "data": excel_utils.get_data()}

@app.put("/actualizar/{fila}")
def actualizar_fila(fila: int, data: DataRow):
    current = excel_utils.get_data()
    if not current:
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    if fila < 2 or fila > len(current):
        raise HTTPException(status_code=400, detail="Fila fuera de rango.")
    if len(data.values) != len(current[0]):
        raise HTTPException(status_code=400, detail=f"Se requieren {len(current[0])} valores.")
    if not excel_utils.update_row(fila, data.values):
        raise HTTPException(status_code=400, detail="No se pudo actualizar la fila.")
    return {"message": f"Fila {fila} actualizada.", "data": excel_utils.get_data()}

@app.delete("/eliminar/{fila}")
def eliminar_fila(fila: int):
    current = excel_utils.get_data()
    if not current:
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    if fila < 2 or fila > len(current):
        raise HTTPException(status_code=400, detail="Fila fuera de rango.")
    if not excel_utils.delete_row(fila):
        raise HTTPException(status_code=400, detail="No se pudo eliminar la fila.")
    return {"message": f"Fila {fila} eliminada.", "data": excel_utils.get_data()}

@app.get("/datos")
def obtener_datos():
    data = excel_utils.get_data()
    if not data:
        raise HTTPException(status_code=404, detail="Archivo no encontrado o vacío.")
    return {"data": data}