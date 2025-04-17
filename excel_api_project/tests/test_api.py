import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.excel_utils import EXCEL_FILE

client = TestClient(app)

@pytest.fixture(autouse=True)
def cleanup_excel():
    # Elimina el archivo antes y después de cada test
    if os.path.exists(EXCEL_FILE):
        os.remove(EXCEL_FILE)
    yield
    if os.path.exists(EXCEL_FILE):
        os.remove(EXCEL_FILE)

def test_crear_excel():
    response = client.post("/crear_excel", json={"headers": ["Nombre", "Edad"]})
    assert response.status_code == 200
    assert response.json()["headers"] == ["Nombre", "Edad"]

def test_insertar_y_obtener():
    client.post("/crear_excel", json={"headers": ["Nombre", "Edad"]})
    response = client.post("/insertar", json={"values": ["Luis", 30]})
    assert response.status_code == 200
    data = response.json()["data"]
    assert data[1] == ["Luis", 30]

def test_actualizar():
    client.post("/crear_excel", json={"headers": ["Nombre", "Edad"]})
    client.post("/insertar", json={"values": ["Luis", 30]})
    response = client.put("/actualizar/2", json={"values": ["Ana", 25]})
    assert response.status_code == 200
    assert response.json()["data"][1] == ["Ana", 25]

def test_eliminar():
    client.post("/crear_excel", json={"headers": ["Nombre", "Edad"]})
    client.post("/insertar", json={"values": ["Luis", 30]})
    response = client.delete("/eliminar/2")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1  # Solo encabezados

def test_errores():
    # Insertar sin archivo
    response = client.post("/insertar", json={"values": ["Luis", 30]})
    assert response.status_code == 404
    # Actualizar fila inexistente
    client.post("/crear_excel", json={"headers": ["Nombre", "Edad"]})
    response = client.put("/actualizar/5", json={"values": ["Ana", 25]})
    assert response.status_code == 400