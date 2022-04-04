CREATE USER 'cto' IDENTIFIED BY 'millionaire11';

CREATE SCHEMA CP;

CREATE TABLE CP.users
LIKE amanel.usuarios;

INSERT CP.users
SELECT *
FROM amanel.usuarios
WHERE idusuarios BETWEEN 2200 AND 2277;

INSERT grupal_db.contactos
SELECT usuarios.id_usuarios, usuarios.telefono
FROM grupal_db.usuarios;

#, contraseña, zona horaria (por defecto UTC-3), género
ALTER TABLE `cp`.`users` 
DROP COLUMN `FechaRegistro`,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(20) NOT NULL ;

ALTER TABLE `cp`.`users` 
ADD COLUMN `Gender` VARCHAR(3) NOT NULL AFTER `Phone`,
ADD COLUMN `Time_Zone` VARCHAR(33) NOT NULL AFTER `Gender`,
ADD COLUMN `Password` VARCHAR(12) NOT NULL AFTER `Surname`,
CHANGE COLUMN `idusuarios` `user_id` INT NOT NULL AUTO_INCREMENT ,
CHANGE COLUMN `Nombre` `Name` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Apellido` `Surname` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Email` `Email` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Telefono` `Phone` VARCHAR(15) NOT NULL ;

SET @@session.time_zone = "-03:00";

UPDATE `cp`.`users` SET `Password` = 'Sam4587UK', `Gender` = 'M', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2200');
UPDATE `cp`.`users` SET `Password` = 'Flo98ARG', `Gender` = 'F', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2211');
UPDATE `cp`.`users` SET `Password` = 'Lala1511N', `Gender` = 'F', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2222');
UPDATE `cp`.`users` SET `Password` = 'DanyBA33', `Gender` = 'M', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2233');
UPDATE `cp`.`users` SET `Password` = 'Alerci2004', `Gender` = 'M', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2244');
UPDATE `cp`.`users` SET `Password` = 'Javy3997', `Gender` = 'F', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2255');
UPDATE `cp`.`users` SET `Password` = 'Nany1212', `Gender` = 'F', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2266');
UPDATE `cp`.`users` SET `Password` = 'Oli29915', `Gender` = 'F', `Time_Zone` = @@session.time_zone  WHERE (`user_id` = '2277');

# 2nda tabla info = join_id, user_id y la join_DT 
CREATE TABLE `cp`.`sign_in` (
  `join_id` INT NOT NULL auto_increment,
  `user_id` INT NOT NULL,
  `join_DT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`join_id`),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `cp`.`users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
 
ALTER TABLE sign_in auto_increment= 3300;

INSERT INTO sign_in (`user_id`) VALUES (2200),
(2211),	
(2222),
(2233),
(2244),
(2255),	
(2266),	
(2277);	


#3era tabla info = visit_times, Piense en una estructura de columnas que permita entregar esta información y cree la tabla.
SELECT
  user_id,join_DT,
  COUNT(join_DT) AS `visit_times` 
FROM
 sign_in
GROUP BY 
  join_DT;

#Como tengo la FK en cascada, 
#si borro una tabla afectará las otras. 
#Así que no lo haré. Gracias.
#Buenas Noches








#WORK IN PROGRESS


#default= COUNT(cp.sign_in),
#CREATE TABLE `cp`.`visits` (
#  `id` INT NOT NULL,
#  `Total_visits` INT NOT NULL  
#  PRIMARY KEY (`id`),
#  CONSTRAINT `id`
#    FOREIGN KEY (`user_id`)
#    REFERENCES `cp`.`sign_in` (`user_id`)
#    ON DELETE CASCADE
#    ON UPDATE CASCADE);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
INSERT INTO visits (`user_id`) VALUES (2200),
(2211),	
(2222),
(2233),
(2244),
(2255),	
(2266),	
(2277);	


#SELECT
  #CONVERT_TZ('2007-03-11 2:00:00','US/Eastern','US/Central') AS time1,
  #CONVERT_TZ('2007-03-11 3:00:00','US/Eastern','US/Central') AS time2;
