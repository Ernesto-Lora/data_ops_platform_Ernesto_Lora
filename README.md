# ETL Pipeline con Python, PostgreSQL y Docker

Este proyecto implementa un flujo ETL (Extracción, Transformación y Carga) usando Python, `pandas` y SQLAlchemy para procesar datos financieros desde un archivo CSV y cargarlos en una base de datos PostgreSQL.

---

## ⚙️ Requisitos

- Docker

---

## 🔐 Variables de Entorno

Asegúrate de tener un archivo `.env` con las siguientes variables configuradas:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mi_base_de_datos
DB_USER=usuario
DB_PASSWORD=contraseña
```

Se puede utilizar el archivo `.env.example`:

---

## 🐳 Ejecución con Docker

### 1. Construir y ejecutar el contenedor.

```bash
docker-compose up --build -d .
```

## 📊 Flujo del ETL

1. **Extracción**  
   Se lee un archivo CSV (`/app/data/financial_transactions.csv`) utilizando `pandas`.

2. **Transformación**  
   Los datos se limpian y transforman (ver `transform.py`).

3. **Carga**  
   Los datos transformados se cargan en una base de datos PostgreSQL usando `SQLAlchemy`.

---

## 📦 Dependencias

Las dependencias están definidas en `requirements.txt`, incluyendo:

- pandas
- SQLAlchemy
- python-dotenv
- psycopg2-binary

---

## 📑 Archivos Clave

- `etl_script.py` – Orquestador principal del flujo ETL
- `extract.py` – Lógica para leer datos desde CSV
- `transform.py` – Lógica de transformación y limpieza
- `load.py` – Carga los datos a PostgreSQL
- `db_utils.py` – Maneja la conexión robusta a la base de datos
- `logger.py` – Logger reutilizable con formato estándar
- `config.py` – Centraliza configuración y constantes

---

## 🧪 Pruebas y Desarrollo

Puedes ejecutar el script localmente si tienes las dependencias instaladas:

```bash
python etl_script.py
```

---

## 📝 Notas

- La tabla en PostgreSQL se reemplaza cada vez que se ejecuta el pipeline (`if_exists="replace"`).
- Puedes adaptar fácilmente este flujo para leer desde otras fuentes de datos o aplicar lógicas de transformación más complejas.

---

## 📬 Contacto

¡Con mucho gusto podríamos colaborar!
elg935@gmail.com
