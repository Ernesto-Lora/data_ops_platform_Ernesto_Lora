def load_to_db(df, engine, table_name):
    """
    Carga un DataFrame de pandas en una tabla de base de datos utilizando SQLAlchemy.

    Args:
        df (pd.DataFrame): DataFrame a cargar.
        engine (sqlalchemy.Engine): Conexión SQLAlchemy a la base de datos.
        table_name (str): Nombre de la tabla destino.

    Raises:
        Exception: Si ocurre un error durante la carga.
    """
    from logger import get_logger
    logger = get_logger(__name__)
    
    logger.info(f"Loading data into table: {table_name}")
    try:
        # Reemplaza la tabla si ya existe, sin incluir el índice del DataFrame
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logger.info("Data loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load data into DB: {e}")
        raise
