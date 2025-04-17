# Excel API Project

API REST para crear, insertar, actualizar y eliminar datos en un archivo Excel.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

## Pruebas

```bash
pytest
```

## Endpoints

- `POST /crear_excel` — Crear archivo con encabezados.
- `POST /insertar` — Insertar fila.
- `PUT /actualizar/{fila}` — Actualizar fila.
- `DELETE /eliminar/{fila}` — Eliminar fila.
- `GET /datos` — Obtener datos.