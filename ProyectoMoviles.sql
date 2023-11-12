CREATE TABLE USUARIO (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  usuario     varchar(25) NOT NULL UNIQUE, 
  contrasena  varchar(64) NOT NULL, 
  tipoUsuario char(1) NOT NULL, 
  token       varchar(100) NOT NULL, 
  estadoToken char(1) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE PERSONAL (
  id        int(10) NOT NULL AUTO_INCREMENT, 
  tipoDoc   char(3) NOT NULL, 
  numeroDoc varchar(20) NOT NULL, 
  apellidos varchar(50) NOT NULL, 
  nombres   varchar(50) NOT NULL, 
  direccion varchar(200) NOT NULL, 
  email     varchar(50) NOT NULL, 
  telefono  varchar(12) NOT NULL, 
  estado    char(1) NOT NULL, 
  fechaNac  date NOT NULL, 
  USUARIOid int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE CLIENTE (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  tipoDoc     char(3) NOT NULL, 
  numeroDoc   varchar(20) NOT NULL, 
  nombres     varchar(50), 
  razonSocial varchar(50), 
  direccion   varchar(200) NOT NULL, 
  email       varchar(50) NOT NULL, 
  telefono    varchar(12) NOT NULL, 
  estado      char(1) NOT NULL, 
  USUARIOid   int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE SOLICITUD_SERVICIO (
  id               int(10) NOT NULL AUTO_INCREMENT, 
  descripcionCarga text NOT NULL, 
  claseCarga       char(1) NOT NULL, 
  tipoCarga        char(1) NOT NULL, 
  categoriaCarga   char(2) NOT NULL, 
  pesoKg           numeric(9, 2) NOT NULL, 
  fechaHoraPartida timestamp NOT NULL, 
  fechaHoraLlegada timestamp NOT NULL, 
  direccionOrigen  varchar(255) NOT NULL, 
  direccionDestino varchar(255) NOT NULL, 
  mantoPagar       numeric(9, 2) NOT NULL, 
  distanciaKm      numeric(9, 2) NOT NULL, 
  TARIFAid         int(10) NOT NULL, 
  CLIENTEid        int(10) NOT NULL, 
  PAGO_SOLICITUDid int(10), 
  PRIMARY KEY (id));
CREATE TABLE PAGO_SOLICITUD (
  id                 int(10) NOT NULL AUTO_INCREMENT, 
  nombreEntidad      varchar(50) NOT NULL, 
  numOperacion       char(8) NOT NULL, 
  fechaHoraOperacion timestamp NOT NULL, 
  urlVoucher         varchar(150) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE ESTADO_SOLICITUD (
  id                   int(10) NOT NULL AUTO_INCREMENT, 
  nombreEstado         varchar(50) NOT NULL, 
  fechaHoraRegistro    timestamp NOT NULL, 
  observacion          text NOT NULL, 
  estado               char(1) NOT NULL, 
  SOLICITUD_SERVICIOid int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE TARIFA (
  id              int(10) NOT NULL AUTO_INCREMENT, 
  tarifa          numeric(5, 2) NOT NULL, 
  estado          char(1) NOT NULL, 
  fechaHoraInicio timestamp NOT NULL, 
  fechaHoraFin    timestamp NULL, 
  PRIMARY KEY (id));
CREATE TABLE CONDUCTOR (
  id        int(10) NOT NULL AUTO_INCREMENT, 
  tipoDoc   char(3) NOT NULL, 
  numeroDoc varchar(20) NOT NULL, 
  apellidos varchar(50) NOT NULL, 
  nombres   varchar(50) NOT NULL, 
  direccion varchar(200) NOT NULL, 
  fechaNac  date NOT NULL, 
  estado    char(1) NOT NULL, 
  USUARIOid int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE VEHICULO (
  id             int(10) NOT NULL AUTO_INCREMENT, 
  matricula      char(7) NOT NULL, 
  capacidadTotal numeric(9, 2) NOT NULL, 
  tipoCarga      char(1) NOT NULL, 
  modelo         varchar(50) NOT NULL, 
  marca          varchar(50) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE VEHICULO_CONDUCTOR (
  SOLICITUD_SERVICIOid int(10) NOT NULL, 
  VEHICULOid           int(10) NOT NULL, 
  CONDUCTORid          int(10) NOT NULL, 
  latitud              numeric(9, 5), 
  longitud             numeric(9, 5), 
  nombreEstado         varchar(50), 
  fechaHoraRegistro    timestamp NULL, 
  observacion          text, 
  PRIMARY KEY (SOLICITUD_SERVICIOid, 
  VEHICULOid, 
  CONDUCTORid));
ALTER TABLE VEHICULO_CONDUCTOR ADD CONSTRAINT FKVEHICULO_C622019 FOREIGN KEY (VEHICULOid) REFERENCES VEHICULO (id);
ALTER TABLE VEHICULO_CONDUCTOR ADD CONSTRAINT FKVEHICULO_C127842 FOREIGN KEY (CONDUCTORid) REFERENCES CONDUCTOR (id);
ALTER TABLE CLIENTE ADD CONSTRAINT FKCLIENTE555484 FOREIGN KEY (USUARIOid) REFERENCES USUARIO (id);
ALTER TABLE PERSONAL ADD CONSTRAINT FKPERSONAL775969 FOREIGN KEY (USUARIOid) REFERENCES USUARIO (id);
ALTER TABLE CONDUCTOR ADD CONSTRAINT FKCONDUCTOR116504 FOREIGN KEY (USUARIOid) REFERENCES USUARIO (id);
ALTER TABLE SOLICITUD_SERVICIO ADD CONSTRAINT FKSOLICITUD_899861 FOREIGN KEY (TARIFAid) REFERENCES TARIFA (id);
ALTER TABLE SOLICITUD_SERVICIO ADD CONSTRAINT FKSOLICITUD_878765 FOREIGN KEY (PAGO_SOLICITUDid) REFERENCES PAGO_SOLICITUD (id);
ALTER TABLE VEHICULO_CONDUCTOR ADD CONSTRAINT FKVEHICULO_C166246 FOREIGN KEY (SOLICITUD_SERVICIOid) REFERENCES SOLICITUD_SERVICIO (id);
ALTER TABLE SOLICITUD_SERVICIO ADD CONSTRAINT FKSOLICITUD_53103 FOREIGN KEY (CLIENTEid) REFERENCES CLIENTE (id);
ALTER TABLE ESTADO_SOLICITUD ADD CONSTRAINT FKESTADO_SOL268616 FOREIGN KEY (SOLICITUD_SERVICIOid) REFERENCES SOLICITUD_SERVICIO (id);
