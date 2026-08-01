-- phpMyAdmin SQL Dump
-- JOINS practice DB

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

DROP DATABASE IF EXISTS `practica_joins`;
CREATE DATABASE IF NOT EXISTS `practica_joins` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `practica_joins`;

-- Tabla usuarios
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `direccion_id`) VALUES
(1, 'Juan', 'Perez', 1),
(2, 'Ana', 'Gomez', 2),
(3, 'Carlos', 'Lopez', NULL);

-- Tabla direcciones
CREATE TABLE `direcciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(100) NOT NULL,
  `colonia` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `pais` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `direcciones` (`id`, `calle`, `colonia`, `ciudad`, `pais`) VALUES
(1, 'Av. Reforma 123', 'Centro', 'Ciudad de México', 'México'),
(2, 'Calle Falsa 456', 'Nápoles', 'Ciudad de México', 'México');

-- Tabla pedidos
CREATE TABLE `pedidos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `total` float NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `pedidos` (`id`, `fecha`, `total`, `usuario_id`) VALUES
(1, '2024-04-01 10:00:00', 16000, 1),
(2, '2024-04-02 15:30:00', 1500, 2);

-- Tabla productos
CREATE TABLE `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `productos` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Laptop', 'Laptop de 15 pulgadas'),
(2, 'Mouse inalámbrico', 'Mouse inalámbrico Bluetooth');

-- Tabla pedidos_has_productos
CREATE TABLE `pedidos_has_productos` (
  `pedido_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  PRIMARY KEY (`pedido_id`, `producto_id`)
);

INSERT INTO `pedidos_has_productos` (`pedido_id`, `producto_id`) VALUES
(1, 1),
(1, 2),
(2, 2);

-- Claves Foráneas
ALTER TABLE `usuarios`
  ADD FOREIGN KEY (`direccion_id`) REFERENCES `direcciones` (`id`) ON DELETE SET NULL;

ALTER TABLE `pedidos`
  ADD FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

ALTER TABLE `pedidos_has_productos`
  ADD FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`),
  ADD FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`);

COMMIT;