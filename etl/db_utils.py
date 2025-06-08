from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import time
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, MAX_RETRIES, RETRY_DELAY
from logger import get_logger

# Inicializa el logger para registrar eventos en este módulo
logger = get_logger(__name__)

def connect_to_db():
    """
    Intenta conectarse a una base de datos PostgreSQL usando SQLAlchemy.
    Realiza varios intentos si la conexión falla, con un tiempo de espera entre intentos.

    Returns:
        engine (sqlalchemy.Engine): Objeto de conexión a la base de datos.

    Raises:
        ConnectionError: Si no se puede establecer conexión después del número máximo de reintentos.
    """
    engine_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    logger.info(f"Connecting to DB at {DB_HOST}:{DB_PORT}/{DB_NAME}")

    last_exception = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # Crear engine SQLAlchemy
            engine = create_engine(engine_url, pool_pre_ping=True)
            
            # Intentar conectar y ejecutar una consulta simple para validar la conexión
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            logger.info("Connected to database.")
            return engine

        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt} failed: {e}")
            time.sleep(RETRY_DELAY)

    # Si todos los intentos fallan, registrar error y lanzar excepción
    logger.error("Could not connect to the database after retries.")
    raise ConnectionError("Failed to connect to the database.") from last_exception

