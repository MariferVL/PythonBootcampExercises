-- Borrar y Crear basedatos
DROP DATABASE IF EXISTS TLV_5_5;
CREATE DATABASE IF NOT EXISTS TLV_5_5;


USE TLV_5_5;
SET @@session.time_zone = "-03:00";











-- Borrar y Crear basedatos

DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (
	id_usuario int NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(111) NOT NULL,
	apellido VARCHAR(111) NOT NULL,
	contrasena VARCHAR(111) NOT NULL,
	zona_horaria VARCHAR(111) NOT NULL,
	genero VARCHAR(111) NOT NULL,
	telefono_de_contacto VARCHAR(111) NOT NULL,
	PRIMARY KEY (id_usuario)
);

ALTER TABLE `tlv_5_5`.`usuarios` 
DROP PRIMARY KEY,
ADD PRIMARY KEY (`id_usuario`, `telefono_de_contacto`);
;


DROP TABLE IF EXISTS informacion;
CREATE TABLE informacion (
	id_ingreso INT NOT NULL AUTO_INCREMENT,
    -- fecha_hora_de_ingreso INT NOT NULL,
    fecha_hora_de_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP,
    fk_id_usuario INT NOT NULL,
    PRIMARY KEY(id_ingreso),
	FOREIGN KEY (fk_id_usuario) REFERENCES usuarios(id_usuario)
);

SET @@session.time_zone = "-02:00";

INSERT INTO usuarios (nombre, apellido, contrasena, zona_horaria, genero, telefono_de_contacto)
	VALUES	('andres', 'alvarez', '1234', @@session.time_zone, 'M', '56912123341'),
 			('beatriz', 'burgos', '1234', @@session.time_zone, 'F', '56922123342'),
			('camilo','caceres','1234',@@session.time_zone,'M','56932123343'),
			('danilo','diaz','1234',@@session.time_zone,'M','56942123344'),
			('eva','enrriquez','1234',@@session.time_zone,'F','56952123345'),
			('fernando','fernandez','1234',@@session.time_zone,'M','56962123345'),
			('gabriela','godinez','1234',@@session.time_zone,'F','56972123344'),
			('hilda','higuain','1234',@@session.time_zone,'F','56982123344');

INSERT INTO informacion (fk_id_usuario)
	VALUES	(2),
			(2),
            (4),
            (4),
            (3),
			(1),
            (5),
            (2);



DROP TABLE IF EXISTS contactos;
CREATE TABLE contactos (
  `id_contacto` INT NOT NULL AUTO_INCREMENT,
  `fk_id_usuario` INT NOT NULL,
  `fk_telefono` VARCHAR(45) NOT NULL,
  `correo_electronico` VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_contacto),
  INDEX (fk_id_usuario, fk_telefono ),
  FOREIGN KEY (fk_id_usuario, fk_telefono)
 REFERENCES usuarios (id_usuario, telefono_de_contacto)
    ON DELETE CASCADE ON UPDATE CASCADE)
    ENGINE=INNODB;

#InnoDB actualmente no admite FK para tablas con particiones definidas por el usuario. 
#Esto incluye tanto tablas primarias como secundarias.
#Una tabla en una relación de FK no se puede modificar para usar otro motor de almacenamiento. 
#Para cambiar el motor de almacenamiento, primero debe descartar cualquier restricción de clave externa.

INSERT INTO contactos (fk_id_usuario, fk_telefono, correo_electronico)
VALUES	(1,'56912123341','andres@mail.com'),
			(2,'56922123342','beatriz@mail.com'),
            (3,'56932123343','camilo@mail.com'),
            (4,'56942123344','danilo@mail.com'),
            (5,'56952123345','eva@mail.com'),
            (6,'56962123345','fernando@mail.com'),
            (7,'56972123344','gabriela@mail.com'),
            (8,'56982123344','hilda@mail.com');


-- SELECT * FROM usuarios;
-- SELECT * FROM informacion;
SELECT * FROM contactos;


