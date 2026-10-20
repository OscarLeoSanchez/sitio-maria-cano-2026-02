-- datos.sql
-- Datos de la base "ventas". Ejecutar despues de esquema.sql, con las tablas vacias.
-- Los ids 1 a 5 de cliente, 1 a 4 de producto, 1 a 3 de categoria y 101 a 103 de pedido
-- son los de la Unidad 3. Los demas son nuevos.

USE ventas;

INSERT INTO categoria (id_categoria, nombre)
VALUES
    (1, 'Periféricos'),
    (2, 'Pantallas'),
    (3, 'Fotografía'),
    (4, 'Audio'),
    (5, 'Accesorios');

INSERT INTO producto (id_producto, nombre, precio, stock, id_categoria)
VALUES
    (1,  'Mouse',               80000,   20, 1),
    (2,  'Monitor',             900000,   4, 2),
    (3,  'Teclado',             150000,  15, 1),
    (4,  'Cámara',              500000,   3, 3),
    (5,  'Webcam HD',           180000,   9, 1),
    (6,  'Mouse gamer',         120000,   7, 1),
    (7,  'Hub USB',              60000,  30, 1),
    (8,  'Monitor 27 pulgadas', 1400000,  0, 2),
    (9,  'Pantalla portátil',   750000,   5, 2),
    (10, 'Cámara réflex',       2500000,  2, 3),
    (11, 'Trípode',             120000,   8, 3),
    (12, 'Lente 50 mm',         650000,   3, 3),
    (13, 'Audífonos',           200000,  14, 4),
    (14, 'Parlante bluetooth',  180000,  11, 4),
    (15, 'Micrófono USB',       250000,   6, 4),
    (16, 'Barra de sonido',     500000,   4, 4),
    (17, 'Cable HDMI',           25000,  80, 5),
    (18, 'Base refrigerante',    70000,  12, 5);

INSERT INTO cliente (id_cliente, nombre, correo, ciudad, fecha_registro)
VALUES
    (1,  'Ana',       'ana@email.com',         'Medellín', '2024-02-10'),
    (2,  'Carlos',    'carlos@email.com',      'Bogotá',   '2024-05-22'),
    (3,  'Laura',     'laura@email.com',       'Cali',     '2024-09-03'),
    (4,  'Juan',      'juan@email.com',        'Medellín', '2025-01-15'),
    (5,  'Sara',      'sara@email.com',        'Bogotá',   '2025-04-30'),
    (6,  'Pedro',     NULL,                    'Cali',     '2025-08-19'),
    (7,  'Carlos',    'carlos.m@gmail.com',    'Medellín', '2025-11-02'),
    (8,  'Marta',     NULL,                    'Bogotá',   '2026-03-14'),
    (9,  'Diego',     'diego@correo.co',       NULL,       '2026-06-01'),
    (10, 'Valentina', 'valentina@gmail.com',   NULL,       '2026-09-15');

-- El jefe se inserta antes que sus subordinados.
INSERT INTO empleado (id_empleado, nombre, cargo, salario, fecha_ingreso, id_jefe)
VALUES
    (1, 'Gloria Restrepo',  'Gerente',        9000000, '2019-03-01', NULL),
    (2, 'Andrés Vélez',     'Jefe de ventas', 5500000, '2020-06-15', 1),
    (3, 'Camila Torres',    'Jefe de ventas', 5500000, '2021-01-10', 1),
    (4, 'Felipe Arias',     'Vendedor',       3200000, '2022-02-01', 2),
    (5, 'Natalia Ruiz',     'Vendedor',       3200000, '2022-08-16', 2),
    (6, 'Sebastián Gómez',  'Vendedor',       3000000, '2023-05-02', 2),
    (7, 'Daniela Ocampo',   'Vendedor',       3000000, '2024-01-15', 3),
    (8, 'Mateo Giraldo',    'Vendedor',       2800000, '2025-03-03', 3);

INSERT INTO pedido (id_pedido, fecha, estado, id_cliente, id_empleado)
VALUES
    (101, '2026-09-20', 'pendiente', 1, 4),
    (102, '2026-09-21', 'pagado',    2, 5),
    (103, '2026-09-21', 'pagado',    1, 4),
    (104, '2026-09-23', 'pagado',    3, 6),
    (105, '2026-09-25', 'enviado',   5, 7),
    (106, '2026-09-27', 'enviado',   1, 5),
    (107, '2026-09-28', 'pagado',    2, 8),
    (108, '2026-09-30', 'pagado',    3, 6),
    (109, '2026-10-02', 'enviado',   6, 4),
    (110, '2026-10-05', 'pagado',    4, 5),
    (111, '2026-10-08', 'enviado',   7, 7),
    (112, '2026-10-10', 'pagado',    3, 6),
    (113, '2026-10-12', 'pagado',    1, 5),
    (114, '2026-10-13', 'cancelado', 9, 2),
    (115, '2026-10-14', 'enviado',   5, 4),
    (116, '2026-10-15', 'pagado',    2, 5),
    (117, '2026-10-16', 'pagado',    3, 8),
    (118, '2026-10-17', 'pendiente', 8, 7),
    (119, '2026-10-17', 'pagado',    1, 6),
    (120, '2026-10-18', 'enviado',   4, 4),
    (121, '2026-10-18', 'pagado',    7, 5),
    (122, '2026-10-19', 'pagado',    2, 8),
    (123, '2026-10-19', 'enviado',   3, 7),
    (124, '2026-10-19', 'pagado',    6, 4),
    (125, '2026-10-19', 'pendiente', 5, 6);

-- precio_unitario es el precio al momento de vender. En tres lineas difiere del precio actual
-- del producto: es una instantanea, no un dato derivable.
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
VALUES
    (101, 1,  2, 80000),   (101, 3,  1, 150000),
    (102, 2,  1, 900000),
    (103, 4,  1, 500000),  (103, 1,  1, 80000),
    (104, 5,  1, 190000),  (104, 1,  1, 80000),  (104, 17, 3, 25000),
    (105, 8,  1, 1500000), (105, 9,  1, 750000), (105, 16, 1, 500000),
    (106, 13, 1, 200000),  (106, 15, 1, 250000),
    (107, 10, 1, 2500000), (107, 11, 1, 120000), (107, 12, 1, 650000),
    (108, 3,  2, 150000),  (108, 6,  1, 120000), (108, 1,  1, 80000),
    (109, 16, 1, 500000),  (109, 13, 2, 200000),
    (110, 2,  2, 900000),  (110, 7,  1, 60000),
    (111, 14, 2, 180000),  (111, 17, 2, 25000),
    (112, 4,  1, 500000),  (112, 11, 1, 120000),
    (113, 1,  3, 80000),   (113, 7,  2, 60000),  (113, 17, 5, 25000),
    (114, 8,  1, 1500000),
    (115, 3,  1, 150000),  (115, 5,  1, 180000),
    (116, 15, 1, 250000),  (116, 6,  2, 120000),
    (117, 9,  2, 750000),  (117, 3,  1, 150000),
    (118, 1,  1, 80000),   (118, 17, 2, 25000),
    (119, 8,  1, 1400000), (119, 13, 1, 200000),
    (120, 13, 1, 200000),  (120, 14, 1, 180000), (120, 16, 1, 500000),
    (121, 12, 1, 650000),  (121, 10, 1, 2500000),(121, 17, 1, 25000),
    (122, 5,  2, 180000),  (122, 7,  1, 60000),
    (123, 2,  1, 900000),  (123, 3,  1, 150000), (123, 16, 1, 500000),
    (124, 1,  2, 80000),   (124, 6,  1, 120000),
    (125, 11, 2, 120000),  (125, 4,  1, 500000);
