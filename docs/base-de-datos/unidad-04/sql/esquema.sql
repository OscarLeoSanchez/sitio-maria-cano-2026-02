-- esquema.sql
-- Base de datos "ventas" para MySQL 8.4.
-- Se puede ejecutar varias veces: cada sentencia usa IF NOT EXISTS y no pierde datos.

CREATE DATABASE IF NOT EXISTS ventas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;

USE ventas;

-- Tablas que no dependen de ninguna otra.

CREATE TABLE IF NOT EXISTS categoria (
    id_categoria  INT          NOT NULL AUTO_INCREMENT,
    nombre        VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_categoria),
    UNIQUE (nombre)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente      INT          NOT NULL AUTO_INCREMENT,
    nombre          VARCHAR(100) NOT NULL,
    correo          VARCHAR(150),
    ciudad          VARCHAR(80),
    fecha_registro  DATE         NOT NULL DEFAULT (CURRENT_DATE),
    PRIMARY KEY (id_cliente),
    UNIQUE (correo)
) ENGINE = InnoDB;

-- empleado apunta a si misma: id_jefe es el id_empleado del jefe.

CREATE TABLE IF NOT EXISTS empleado (
    id_empleado    INT           NOT NULL AUTO_INCREMENT,
    nombre         VARCHAR(100)  NOT NULL,
    cargo          VARCHAR(60)   NOT NULL,
    salario        DECIMAL(10,2) NOT NULL,
    fecha_ingreso  DATE          NOT NULL,
    id_jefe        INT,
    PRIMARY KEY (id_empleado),
    CONSTRAINT fk_empleado_jefe
        FOREIGN KEY (id_jefe) REFERENCES empleado (id_empleado)
        ON DELETE SET NULL
) ENGINE = InnoDB;

-- Tablas que dependen de las anteriores.

CREATE TABLE IF NOT EXISTS producto (
    id_producto   INT           NOT NULL AUTO_INCREMENT,
    nombre        VARCHAR(100)  NOT NULL,
    precio        DECIMAL(10,2) NOT NULL,
    stock         INT           NOT NULL DEFAULT 0,
    id_categoria  INT,
    PRIMARY KEY (id_producto),
    CONSTRAINT chk_producto_precio CHECK (precio >= 0),
    CONSTRAINT chk_producto_stock  CHECK (stock >= 0),
    CONSTRAINT fk_producto_categoria
        FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS pedido (
    id_pedido    INT  NOT NULL AUTO_INCREMENT,
    fecha        DATE NOT NULL,
    estado       ENUM('pendiente', 'pagado', 'enviado', 'cancelado')
                 NOT NULL DEFAULT 'pendiente',
    id_cliente   INT  NOT NULL,
    id_empleado  INT  NOT NULL,
    PRIMARY KEY (id_pedido),
    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        ON DELETE RESTRICT,
    CONSTRAINT fk_pedido_empleado
        FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado)
        ON DELETE RESTRICT
) ENGINE = InnoDB;

-- Tabla intermedia entre pedido y producto, con clave primaria compuesta.

CREATE TABLE IF NOT EXISTS detalle_pedido (
    id_pedido        INT           NOT NULL,
    id_producto      INT           NOT NULL,
    cantidad         INT           NOT NULL,
    precio_unitario  DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_pedido, id_producto),
    CONSTRAINT chk_detalle_cantidad CHECK (cantidad > 0),
    CONSTRAINT chk_detalle_precio   CHECK (precio_unitario >= 0),
    CONSTRAINT fk_detalle_pedido
        FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido)
        ON DELETE CASCADE,
    CONSTRAINT fk_detalle_producto
        FOREIGN KEY (id_producto) REFERENCES producto (id_producto)
        ON DELETE RESTRICT
) ENGINE = InnoDB;
