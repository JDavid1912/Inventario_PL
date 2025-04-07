import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="inventario",     # Asegúrate de que esta base exista
        user="postgres",           # Tu usuario de PostgreSQL
        password="Luna12"   # Cámbialo por tu contraseña real
    )

def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        with open("./BD/schema.sql", "r") as archivo:
            sql = archivo.read()
            cursor.execute(sql)
            conn.commit()
        print(" Tablas creadas correctamente.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(" Error al crear las tablas:", e)

# Ejecutar si se corre directamente
if __name__ == "__main__":
    init_db()
