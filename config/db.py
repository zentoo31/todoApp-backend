import psycopg2
from config.config import DB_STR

def connect():
    try:
        dsn = DB_STR
        conn = psycopg2.connect(dsn)
        print("¡Se ha conectado a la base de datos!")
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

