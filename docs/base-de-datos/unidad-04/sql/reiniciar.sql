-- reiniciar.sql
-- Borra las seis tablas de la base "ventas" en el orden inverso al de su creacion.
-- Despues, ejecuta esquema.sql y datos.sql para volver al punto de partida.

USE ventas;

DROP TABLE IF EXISTS detalle_pedido;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS producto;
DROP TABLE IF EXISTS empleado;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS categoria;
