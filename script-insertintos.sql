-- INSERT INTO para la tabla USUARIO
INSERT INTO USUARIO (usuario, contrasena, tipoUsuario, token, estadoToken) VALUES
('usuario1_cliente', 'contrasena1', 'C', 'token1', 'A'),
('usuario2_cliente', 'contrasena2', 'C', 'token2', 'A'),
('usuario3_cliente', 'contrasena3', 'C', 'token3', 'A'),
('usuario4_personal', 'contrasena4', 'P', 'token4', 'A'),
('usuario5_personal', 'contrasena5', 'P', 'token5', 'A'),
('usuario6_personal', 'contrasena6', 'P', 'token6', 'A');

-- INSERT INTO para la tabla PERSONAL
INSERT INTO PERSONAL (tipoDoc, numeroDoc, apellidos, nombres, direccion, email, telefono, estado, fechaNac, USUARIOid) VALUES
('DNI', '12345678', 'Apellido1', 'Nombre1', 'Direccion1', 'email1@example.com', '123456789', 'A', '1990-01-01', 4),
('DNI', '98765432', 'Apellido2', 'Nombre2', 'Direccion2', 'email2@example.com', '987654321', 'A', '1985-05-15', 5),
('DNI', '87654321', 'Apellido3', 'Nombre3', 'Direccion3', 'email3@example.com', '111222333', 'A', '1988-10-20', 6);

-- INSERT INTO para la tabla CLIENTE
INSERT INTO CLIENTE (tipoDoc, numeroDoc, nombres, razonSocial, direccion, email, telefono, estado, USUARIOid) VALUES
('DNI', '11111111', 'Cliente1', NULL, 'DireccionCliente1', 'cliente1@example.com', '111111111', 'A', 1),
('RUC', '22222222', NULL, 'RazonSocial2', 'DireccionCliente2', 'cliente2@example.com', '222222222', 'A', 2),
('DNI', '33333333', 'Cliente3', NULL, 'DireccionCliente3', 'cliente3@example.com', '333333333', 'A', 3);

-- INSERT INTO para la tabla TARIFA
INSERT INTO TARIFA (tarifa, estado, fechaHoraInicio, fechaHoraFin) VALUES
(50.00, 'A', '2023-01-01 00:00:00', '2023-12-31 23:59:59'),
(60.00, 'A', '2023-01-01 00:00:00', '2023-12-31 23:59:59'),
(70.00, 'A', '2023-01-01 00:00:00', '2023-12-31 23:59:59');



-- INSERT INTO para la tabla PAGO_SOLICITUD
INSERT INTO PAGO_SOLICITUD (nombreEntidad, numOperacion, fechaHoraOperacion, urlVoucher) VALUES
('Entidad1', '12345678', '2023-01-01 10:30:00', 'http://url1.com/voucher1'),
('Entidad2', '98765432', '2023-01-02 12:45:00', 'http://url2.com/voucher2'),
('Entidad3', '55555555', '2023-01-03 15:00:00', 'http://url3.com/voucher3');

-- INSERT INTO para la tabla SOLICITUD_SERVICIO
INSERT INTO SOLICITUD_SERVICIO (descripcionCarga, claseCarga, tipoCarga, categoriaCarga, pesoKg, fechaHoraPartida, fechaHoraLlegada, direccionOrigen, direccionDestino, montoPagar, distanciaKm, TARIFAid, CLIENTEid, PAGO_SOLICITUDid) VALUES
('Carga1', 'A', 'B', '01', 1000.00, '2023-01-01 08:00:00', '2023-01-01 16:00:00', 'DireccionOrigen1', 'DireccionDestino1', 80.00, 150.00, 1, 1, 1),
('Carga2', 'B', 'C', '02', 2000.00, '2023-01-02 10:00:00', '2023-01-02 18:00:00', 'DireccionOrigen2', 'DireccionDestino2', 120.00, 200.00, 2, 2, 2),
('Carga3', 'C', 'A', '03', 1500.00, '2023-01-03 12:00:00', '2023-01-03 20:00:00', 'DireccionOrigen3', 'DireccionDestino3', 100.00, 180.00, 3, 3, 3);

-- INSERT INTO para la tabla ESTADO_SOLICITUD
INSERT INTO ESTADO_SOLICITUD (nombreEstado, fechaHoraRegistro, observacion, estado, SOLICITUD_SERVICIOid) VALUES
('Estado1', '2023-01-01 08:30:00', 'ObservacionEstado1', 'A', 1),
('Estado2', '2023-01-02 11:00:00', 'ObservacionEstado2', 'A', 2),
('Estado3', '2023-01-03 13:30:00', 'ObservacionEstado3', 'A', 3);



-- INSERT INTO para la tabla USUARIO (conductor)
INSERT INTO USUARIO (usuario, contrasena, tipoUsuario, token, estadoToken) VALUES
('usuario_conductor1', 'contrasena1', 'C', 'token_conductor1', 'A'),
('usuario_conductor2', 'contrasena2', 'C', 'token_conductor2', 'A'),
('usuario_conductor3', 'contrasena3', 'C', 'token_conductor3', 'A');

-- INSERT INTO para la tabla CONDUCTOR
INSERT INTO CONDUCTOR (tipoDoc, numeroDoc, apellidos, nombres, direccion, fechaNac, estado, USUARIOid) VALUES
('DNI', '44444444', 'Conductor1Apellido', 'Conductor1Nombre', 'DireccionConductor1', '1995-03-10', 'A', 7),
('DNI', '55555555', 'Conductor2Apellido', 'Conductor2Nombre', 'DireccionConductor2', '1987-08-22', 'A', 8),
('DNI', '66666666', 'Conductor3Apellido', 'Conductor3Nombre', 'DireccionConductor3', '1990-05-15', 'A', 9);

-- INSERT INTO para la tabla VEHICULO
INSERT INTO VEHICULO (matricula, capacidadTotal, tipoCarga, modelo, marca) VALUES
('ABC123', 5000.00, 'A', 'Modelo1', 'Marca1'),
('XYZ789', 8000.00, 'B', 'Modelo2', 'Marca2'),
('123ABC', 7000.00, 'C', 'Modelo3', 'Marca3');

-- INSERT INTO para la tabla VEHICULO_CONDUCTOR
INSERT INTO VEHICULO_CONDUCTOR (SOLICITUD_SERVICIOid, VEHICULOid, CONDUCTORid, latitud, longitud, nombreEstado, fechaHoraRegistro, observacion) VALUES
(1, 1, 1, 0.0, 0.0, 'Estado1', '2023-01-01 12:00:00', 'Observacion1'),
(2, 2, 2, 0.0, 0.0, 'Estado2', '2023-01-02 14:30:00', 'Observacion2'),
(3, 3, 3, 0.0, 0.0, 'Estado3', '2023-01-03 16:45:00', 'Observacion3');
