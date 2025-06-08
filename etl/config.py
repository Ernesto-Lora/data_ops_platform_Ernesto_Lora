import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el .env.
load_dotenv()

# Configuración de la base de datos
DB_HOST = os.getenv("DB_HOST")            # Dirección del host de la base de datos
DB_PORT = os.getenv("DB_PORT", "5432")    # Puerto de conexión (por defecto 5432 para PostgreSQL)
DB_NAME = os.getenv("DB_NAME")            # Nombre de la base de datos
DB_USER = os.getenv("DB_USER")            # Usuario para la conexión a la base de datos
DB_PASSWORD = os.getenv("DB_PASSWORD")    # Contraseña para el usuario de la base de datos

# Ruta al archivo CSV de transacciones financieras
CSV_PATH = "/app/data/financial_transactions.csv"

# Nombre de la tabla destino en la base de datos
TABLE_NAME = "financial_transactions"

# Parámetros para lógica de reintentos (por ejemplo, al cargar datos o conectarse a la base)
MAX_RETRIES = 5       # Número máximo de reintentos permitidos
RETRY_DELAY = 5       # Tiempo de espera (en segundos) entre reintentos
