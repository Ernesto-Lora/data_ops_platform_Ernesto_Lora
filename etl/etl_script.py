from config import CSV_PATH, TABLE_NAME
from extract import read_csv
from transform import clean_and_transform
from db_utils import connect_to_db
from load import load_to_db
from logger import get_logger

# Inicializa el logger con el nombre del módulo ETL
logger = get_logger("ETL")

def main():
    """
    Función principal del pipeline ETL.
    Ejecuta los pasos: extracción de datos, transformación y carga a la base de datos.
    """
    logger.info("ETL Job started")
    try:
        # Extraer datos desde un archivo CSV
        df = read_csv(CSV_PATH)

        # Limpiar y transformar los datos
        df_clean = clean_and_transform(df)

        # Conectarse a la base de datos
        engine = connect_to_db()

        # Cargar los datos transformados a la base de datos
        load_to_db(df_clean, engine, TABLE_NAME)

        logger.info("ETL Job completed successfully")

    except Exception as e:
        # Registrar el error completo en caso de falla
        logger.exception("ETL Job failed")

# Ejecutar el pipeline solo si el archivo se corre directamente
if __name__ == "__main__":
    main()
