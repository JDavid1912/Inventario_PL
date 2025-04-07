-- Crear tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(50),
    stock_actual INT DEFAULT 0,
    stock_minimo INT DEFAULT 0,
    fecha_caducidad DATE
);

-- Crear tabla de movimientos (entradas y salidas)
CREATE TABLE movimientos (
    id SERIAL PRIMARY KEY,
    producto_id INT NOT NULL,
    tipo_movimiento VARCHAR(10) CHECK (tipo_movimiento IN ('entrada', 'salida')),
    cantidad INT NOT NULL CHECK (cantidad > 0),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);
