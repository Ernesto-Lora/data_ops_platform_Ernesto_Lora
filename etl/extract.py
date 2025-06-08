import pandas as pd
from logger import get_logger

# Inicializa el logger para este módulo
logger = get_logger(__name__)

def read_csv(csv_path: str) -> pd.DataFrame:
    """
    Lee un archivo CSV desde la ruta especificada y lo carga en un DataFrame de pandas.

    Args:
        csv_path (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame: Datos cargados desde el CSV.

    Raises:
        Exception: Si ocurre un error durante la lectura del archivo.
    """
    logger.info(f"Reading CSV from: {csv_path}")
    try:
        df = pd.read_csv(csv_path)
        logger.info(f"Read {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Error reading CSV: {e}")
        raise
