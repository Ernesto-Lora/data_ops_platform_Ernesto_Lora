import logging

def get_logger(name=__name__):
    """
    Configura y devuelve un logger con un formato estándar.

    Args:
        name (str): Nombre del logger (por defecto, el del módulo llamador).

    Returns:
        logging.Logger: Instancia configurada del logger.
    """
    logger = logging.getLogger(name)

    # Evitar agregar múltiples handlers si ya existen
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Establecer nivel de logging por defecto
        logger.setLevel(logging.INFO)

    return logger
