-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para bdrapidisimo
CREATE DATABASE IF NOT EXISTS `bdrapidisimo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bdrapidisimo`;

-- Volcando estructura para tabla bdrapidisimo.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(25) NOT NULL,
  `contrasena` varchar(64) NOT NULL,
  `tipoUsuario` char(1) NOT NULL,
  `token` varchar(100) NOT NULL,
  `estadoToken` char(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.usuario: ~9 rows (aproximadamente)
INSERT INTO `usuario` (`id`, `usuario`, `contrasena`, `tipoUsuario`, `token`, `estadoToken`) VALUES
	(1, 'usuario1_cliente', 'contrasena1', 'C', 'token1', 'A'),
	(2, 'usuario2_cliente', 'contrasena2', 'C', 'token2', 'A'),
	(3, 'usuario3_cliente', 'contrasena3', 'C', 'token3', 'A'),
	(4, 'usuario4_personal', 'contrasena4', 'P', 'token4', 'A'),
	(5, 'usuario5_personal', 'contrasena5', 'P', 'token5', 'A'),
	(6, 'usuario6_personal', 'contrasena6', 'P', 'token6', 'A'),
	(7, 'usuario_conductor1', 'contrasena1', 'D', 'token_conductor1', 'A'),
	(8, 'usuario_conductor2', 'contrasena2', 'D', 'token_conductor2', 'A'),
	(9, 'usuario_conductor3', 'contrasena3', 'D', 'token_conductor3', 'A');

-- Volcando estructura para tabla bdrapidisimo.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipoDoc` char(3) NOT NULL,
  `numeroDoc` varchar(20) NOT NULL,
  `nombres` varchar(50) DEFAULT NULL,
  `razonSocial` varchar(50) DEFAULT NULL,
  `direccion` varchar(200) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `estado` char(1) NOT NULL,
  `USUARIOid` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKCLIENTE555484` (`USUARIOid`),
  CONSTRAINT `FKCLIENTE555484` FOREIGN KEY (`USUARIOid`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.cliente: ~3 rows (aproximadamente)
INSERT INTO `cliente` (`id`, `tipoDoc`, `numeroDoc`, `nombres`, `razonSocial`, `direccion`, `email`, `telefono`, `estado`, `USUARIOid`) VALUES
	(1, 'DNI', '11111111', 'Cliente1', NULL, 'DireccionCliente1', 'cliente1@example.com', '111111111', 'A', 1),
	(2, 'RUC', '22222222', NULL, 'RazonSocial2', 'DireccionCliente2', 'cliente2@example.com', '222222222', 'A', 2),
	(3, 'DNI', '33333333', 'Cliente3', NULL, 'DireccionCliente3', 'cliente3@example.com', '333333333', 'A', 3);

-- Volcando estructura para tabla bdrapidisimo.conductor
CREATE TABLE IF NOT EXISTS `conductor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipoDoc` char(3) NOT NULL,
  `numeroDoc` varchar(20) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `fechaNac` date NOT NULL,
  `estado` char(1) NOT NULL,
  `USUARIOid` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKCONDUCTOR116504` (`USUARIOid`),
  CONSTRAINT `FKCONDUCTOR116504` FOREIGN KEY (`USUARIOid`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.conductor: ~3 rows (aproximadamente)
INSERT INTO `conductor` (`id`, `tipoDoc`, `numeroDoc`, `apellidos`, `nombres`, `direccion`, `fechaNac`, `estado`, `USUARIOid`) VALUES
	(1, 'DNI', '44444444', 'Conductor1Apellido', 'Conductor1Nombre', 'DireccionConductor1', '1995-03-10', 'A', 7),
	(2, 'DNI', '55555555', 'Conductor2Apellido', 'Conductor2Nombre', 'DireccionConductor2', '1987-08-22', 'A', 8),
	(3, 'DNI', '66666666', 'Conductor3Apellido', 'Conductor3Nombre', 'DireccionConductor3', '1990-05-15', 'A', 9);


-- Volcando estructura para tabla bdrapidisimo.tarifa
CREATE TABLE IF NOT EXISTS `tarifa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tarifa` decimal(5,2) NOT NULL,
  `estado` char(1) NOT NULL,
  `fechaHoraInicio` timestamp NOT NULL,
  `fechaHoraFin` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.tarifa: ~3 rows (aproximadamente)
INSERT INTO `tarifa` (`id`, `tarifa`, `estado`, `fechaHoraInicio`, `fechaHoraFin`) VALUES
	(1, 50.00, 'I', '2023-01-01 05:00:00', '2024-01-01 04:59:59'),
	(2, 60.00, 'I', '2023-01-01 05:00:00', '2024-01-01 04:59:59'),
	(3, 70.00, 'A', '2023-01-01 05:00:00', '2024-01-01 04:59:59');

-- Volcando estructura para tabla bdrapidisimo.pago_solicitud
CREATE TABLE IF NOT EXISTS `pago_solicitud` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombreEntidad` varchar(50) NOT NULL,
  `numOperacion` char(8) NOT NULL,
  `fechaHoraOperacion` timestamp NOT NULL,
  `urlVoucher` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.pago_solicitud: ~3 rows (aproximadamente)
INSERT INTO `pago_solicitud` (`id`, `nombreEntidad`, `numOperacion`, `fechaHoraOperacion`, `urlVoucher`) VALUES
	(1, 'Entidad1', '12345678', '2023-01-01 15:30:00', 'http://url1.com/voucher1'),
	(2, 'Entidad2', '98765432', '2023-01-02 17:45:00', 'http://url2.com/voucher2'),
	(3, 'Entidad3', '55555555', '2023-01-03 20:00:00', 'http://url3.com/voucher3');


-- Volcando estructura para tabla bdrapidisimo.solicitud_servicio
CREATE TABLE IF NOT EXISTS `solicitud_servicio` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcionCarga` text NOT NULL,
  `claseCarga` char(1) NOT NULL,
  `tipoCarga` char(1) NOT NULL,
  `categoriaCarga` char(2) NOT NULL,
  `pesoKg` decimal(9,2) NOT NULL,
  `fechaHoraPartida` timestamp NOT NULL,
  `fechaHoraLlegada` timestamp NULL DEFAULT NULL,
  `direccionOrigen` varchar(255) NOT NULL,
  `direccionDestino` varchar(255) NOT NULL,
  `montoPagar` decimal(9,2) NOT NULL,
  `distanciaKm` decimal(9,2) NOT NULL,
  `TARIFAid` int NOT NULL,
  `CLIENTEid` int NOT NULL,
  `PAGO_SOLICITUDid` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKSOLICITUD_899861` (`TARIFAid`),
  KEY `FKSOLICITUD_878765` (`PAGO_SOLICITUDid`),
  KEY `FKSOLICITUD_53103` (`CLIENTEid`),
  CONSTRAINT `FKSOLICITUD_53103` FOREIGN KEY (`CLIENTEid`) REFERENCES `cliente` (`id`),
  CONSTRAINT `FKSOLICITUD_878765` FOREIGN KEY (`PAGO_SOLICITUDid`) REFERENCES `pago_solicitud` (`id`),
  CONSTRAINT `FKSOLICITUD_899861` FOREIGN KEY (`TARIFAid`) REFERENCES `tarifa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.solicitud_servicio: ~3 rows (aproximadamente)
INSERT INTO `solicitud_servicio` (`id`, `descripcionCarga`, `claseCarga`, `tipoCarga`, `categoriaCarga`, `pesoKg`, `fechaHoraPartida`, `fechaHoraLlegada`, `direccionOrigen`, `direccionDestino`, `montoPagar`, `distanciaKm`, `TARIFAid`, `CLIENTEid`, `PAGO_SOLICITUDid`) VALUES
	(1, 'Carga1', 'P', 'C', 'AL', 1000.00, '2023-01-01 13:00:00', '2023-01-01 21:00:00', 'DireccionOrigen1', 'DireccionDestino1', 80.00, 150.00, 1, 1, 1),
	(2, 'Carga2', 'N', 'N', 'MC', 2000.00, '2023-01-02 15:00:00', '2023-01-02 23:00:00', 'DireccionOrigen2', 'DireccionDestino2', 120.00, 200.00, 2, 2, 2),
	(3, 'Carga3', 'P', 'C', 'AL', 1500.00, '2023-01-03 17:00:00', '2023-01-04 01:00:00', 'DireccionOrigen3', 'DireccionDestino3', 100.00, 180.00, 3, 3, 3);


-- Volcando estructura para tabla bdrapidisimo.estado_solicitud
CREATE TABLE IF NOT EXISTS `estado_solicitud` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombreEstado` varchar(50) NOT NULL,
  `fechaHoraRegistro` timestamp NOT NULL,
  `observacion` text NOT NULL,
  `estado` char(1) NOT NULL,
  `SOLICITUD_SERVICIOid` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKESTADO_SOL268616` (`SOLICITUD_SERVICIOid`),
  CONSTRAINT `FKESTADO_SOL268616` FOREIGN KEY (`SOLICITUD_SERVICIOid`) REFERENCES `solicitud_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.estado_solicitud: ~3 rows (aproximadamente)
INSERT INTO `estado_solicitud` (`id`, `nombreEstado`, `fechaHoraRegistro`, `observacion`, `estado`, `SOLICITUD_SERVICIOid`) VALUES
	(1, 'PENDIENTE DE ATENCION', '2023-01-01 13:30:00', 'ObservacionEstado1', 'A', 1),
	(2, 'CONFIRMADO', '2023-01-02 16:00:00', 'ObservacionEstado2', 'A', 2),
	(3, 'PENDIENTE DE ATENCION', '2023-01-03 18:30:00', 'ObservacionEstado3', 'A', 3);

-- Volcando estructura para tabla bdrapidisimo.personal
CREATE TABLE IF NOT EXISTS `personal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipoDoc` char(3) NOT NULL,
  `numeroDoc` varchar(20) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `estado` char(1) NOT NULL,
  `fechaNac` date NOT NULL,
  `USUARIOid` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKPERSONAL775969` (`USUARIOid`),
  CONSTRAINT `FKPERSONAL775969` FOREIGN KEY (`USUARIOid`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.personal: ~3 rows (aproximadamente)
INSERT INTO `personal` (`id`, `tipoDoc`, `numeroDoc`, `apellidos`, `nombres`, `direccion`, `email`, `telefono`, `estado`, `fechaNac`, `USUARIOid`) VALUES
	(1, 'DNI', '12345678', 'Apellido1', 'Nombre1', 'Direccion1', 'email1@example.com', '123456789', 'A', '1990-01-01', 4),
	(2, 'DNI', '98765432', 'Apellido2', 'Nombre2', 'Direccion2', 'email2@example.com', '987654321', 'A', '1985-05-15', 5),
	(3, 'DNI', '87654321', 'Apellido3', 'Nombre3', 'Direccion3', 'email3@example.com', '111222333', 'A', '1988-10-20', 6);



-- Volcando estructura para tabla bdrapidisimo.vehiculo
CREATE TABLE IF NOT EXISTS `vehiculo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matricula` char(7) NOT NULL,
  `capacidadTotal` decimal(9,2) NOT NULL,
  `tipoCarga` char(1) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `marca` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.vehiculo: ~3 rows (aproximadamente)
INSERT INTO `vehiculo` (`id`, `matricula`, `capacidadTotal`, `tipoCarga`, `modelo`, `marca`) VALUES
	(1, 'ABC123', 5000.00, 'A', 'Modelo1', 'Marca1'),
	(2, 'XYZ789', 8000.00, 'B', 'Modelo2', 'Marca2'),
	(3, '123ABC', 7000.00, 'C', 'Modelo3', 'Marca3');

-- Volcando estructura para tabla bdrapidisimo.vehiculo_conductor
CREATE TABLE IF NOT EXISTS `vehiculo_conductor` (
  `SOLICITUD_SERVICIOid` int NOT NULL,
  `VEHICULOid` int NOT NULL,
  `CONDUCTORid` int NOT NULL,
  `latitud` decimal(9,5) DEFAULT NULL,
  `longitud` decimal(9,5) DEFAULT NULL,
  `nombreEstado` varchar(50) DEFAULT NULL,
  `fechaHoraRegistro` timestamp NULL DEFAULT NULL,
  `observacion` text,
  PRIMARY KEY (`SOLICITUD_SERVICIOid`,`VEHICULOid`,`CONDUCTORid`),
  KEY `FKVEHICULO_C622019` (`VEHICULOid`),
  KEY `FKVEHICULO_C127842` (`CONDUCTORid`),
  CONSTRAINT `FKVEHICULO_C127842` FOREIGN KEY (`CONDUCTORid`) REFERENCES `conductor` (`id`),
  CONSTRAINT `FKVEHICULO_C166246` FOREIGN KEY (`SOLICITUD_SERVICIOid`) REFERENCES `solicitud_servicio` (`id`),
  CONSTRAINT `FKVEHICULO_C622019` FOREIGN KEY (`VEHICULOid`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bdrapidisimo.vehiculo_conductor: ~3 rows (aproximadamente)
INSERT INTO `vehiculo_conductor` (`SOLICITUD_SERVICIOid`, `VEHICULOid`, `CONDUCTORid`, `latitud`, `longitud`, `nombreEstado`, `fechaHoraRegistro`, `observacion`) VALUES
	(1, 1, 1, 0.00000, 0.00000, 'VEHICULO EN TRANSITO', '2023-01-01 17:00:00', 'Observacion1'),
	(2, 2, 2, 0.00000, 0.00000, 'VEHICULO DETENIDO ', '2023-01-02 19:30:00', 'Observacion2'),
	(3, 3, 3, 0.00000, 0.00000, 'VEHICULO DETENIDO POR INTERRUPCIÓN', '2023-01-03 21:45:00', 'Observacion3');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
