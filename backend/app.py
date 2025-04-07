from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/productos", methods=["POST"])
def agregar_producto():
    data = request.json
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO productos (nombre, descripcion, categoria, stock_actual, stock_minimo, fecha_caducidad)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data["nombre"],
            data.get("descripcion"),
            data.get("categoria"),
            data.get("stock_actual", 0),
            data.get("stock_minimo", 0),
            data.get("fecha_caducidad")
        ))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Producto agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/productos", methods=["GET"])
def listar_productos():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM productos")
        productos = cur.fetchall()
        columnas = [desc[0] for desc in cur.description]
        resultado = [dict(zip(columnas, fila)) for fila in productos]
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

