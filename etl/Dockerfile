# Usar una imagen base ligera de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para bibliotecas como psycopg2 y pandas
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias Python al contenedor
COPY requirements.txt .

# Instalar dependencias de Python sin usar la caché de pip (reduce el tamaño de la imagen)
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando por defecto al iniciar el contenedor: ejecutar el script principal ETL
CMD ["python", "etl_script.py"]

