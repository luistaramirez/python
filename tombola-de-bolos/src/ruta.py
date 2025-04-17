import os

class Ruta:
    """
    Clase para gestionar las rutas de los archivos y directorios del proyecto.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Directorio base del proyecto
    DATA_DIR = os.path.join(BASE_DIR, "data")  # Directorio 'data'
    EXCEL_FILE = "numeros_generados.xlsx"   # Nombre del archivo Excel

    @staticmethod
    def obtener_ruta_excel(nombre_archivo):
        """
        Obtiene la ruta completa para un archivo Excel en el directorio 'data'.

        Args:
            nombre_archivo (str): Nombre del archivo Excel.

        Returns:
            str: Ruta completa del archivo.
        """
        # Crear el directorio 'data' si no existe
        if not os.path.exists(Ruta.DATA_DIR):
            os.makedirs(Ruta.DATA_DIR)
        return os.path.join(Ruta.DATA_DIR, nombre_archivo)