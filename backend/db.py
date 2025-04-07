import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port="5432",
    database="inventario",
    user="postgres",
    password="Luna12"
)

print("Conexión exitosa a PostgreSQL")

# No olvides cerrar después:
conexion.close()
