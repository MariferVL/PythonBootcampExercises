#DESARROLLO
#Inserte 3 cursos nuevos. 
INSERT INTO `amanel`.`capacitacion` (`CodigoCurso`, `Nombre`, `Horario`, `CostoRealizacion`, `FechaRealizacion`) VALUES ('2211', 'Freedom', '08:00:00', '33000', '2022-11-11');
INSERT INTO `amanel`.`capacitacion` (`CodigoCurso`, `Nombre`, `Horario`, `CostoRealizacion`, `FechaRealizacion`) VALUES ('2222', 'Abundance', '08:00:00', '33000', '2022-12-11');
INSERT INTO `amanel`.`capacitacion` (`CodigoCurso`, `Nombre`, `Horario`, `CostoRealizacion`, `FechaRealizacion`) VALUES ('2223', 'Friendliness', '08:00:00', '33000', '2023-01-11');
UPDATE `amanel`.`capacitacion` SET `Nombre` = 'Fenix', `CostoRealizacion` = '44000' WHERE (`CodigoCurso` = '1111');
UPDATE `amanel`.`capacitacion` SET `CostoRealizacion` = '22000' WHERE (`CodigoCurso` = '1166');
UPDATE `amanel`.`capacitacion` SET `CostoRealizacion` = '22000' WHERE (`CodigoCurso` = '1177');
UPDATE `amanel`.`capacitacion` SET `CostoRealizacion` = '88000' WHERE (`CodigoCurso` = '1199');

#Inserte 3 profesores nuevos
INSERT INTO `amanel`.`operadores` (`RUN`, `Nombre`, `Apellido`, `Direccion`, `Email`, `FechaContrato`) VALUES ('16354877', 'Florencia', 'Rua', 'Rosario', 'teaching@presentes.com', '2022-04-04');
INSERT INTO `amanel`.`operadores` (`RUN`, `Nombre`, `Apellido`, `Direccion`, `Email`, `FechaContrato`) VALUES ('15342987', 'Ada', 'Shummer', 'Berlin', 'ada@presentes.com', '2022-04-04');
INSERT INTO `amanel`.`operadores` (`RUN`, `Nombre`, `Apellido`, `Direccion`, `Email`, `FechaContrato`) VALUES ('20574178', 'Andrés', 'Calamaro', 'Valdivia', 'andres@presentes.com', '2022-04-04');

#¿Cuál es el curso más costoso? Selecciónelo.  Ancestors: $ 88000, A-mor:$ 88000
SELECT Nombre, CostoRealizacion as "Más Costoso" from capacitacion
order by CostoRealizacion desc
limit 3;

#¿Cuál es el profesor con menor salario? Selecciónelo.   R: todos menos Javiera.
ALTER TABLE `amanel`.`operadores` 
ADD COLUMN `Salario_x_curso` INT NOT NULL DEFAULT  88000 AFTER `FechaContrato`;
UPDATE `amanel`.`operadores` SET `Salario(x curso)` = '111000' WHERE (`RUN` = '19654378');

SELECT Nombre, Salario_x_curso as "Menor Salario" from operadores
order by Salario_x_curso asc;

# Seleccione los cursos más costosos que el promedio. 
SELECT Nombre,CostoRealizacion
FROM   capacitacion
where CostoRealizacion > (SELECT AVG(CostoRealizacion ) FROM capacitacion );

#Cree  tabla con cursos menos costosos que el promedio. 
# La tabla debe tener por nombre  "Cursos económicos" 
# Costo Promedio: $40615.3846
 
CREATE TABLE amanel.cursos_economicos 
LIKE amanel.capacitacion;

INSERT amanel.cursos_economicos 
SELECT *
FROM amanel.capacitacion
where CostoRealizacion > (SELECT AVG(CostoRealizacion ) FROM capacitacion );

#2 columnas: ‘ws_quorum’ y ‘public_benefits’(valor menor al costo total del curso).
ALTER TABLE `amanel`.`cursos_economicos` 
ADD COLUMN `ws_quorum` INT NOT NULL DEFAULT 11 AFTER `Course_Name`,
ADD COLUMN `public_benefits` INT NOT NULL DEFAULT 11000 AFTER `ws_quorum`,
CHANGE COLUMN `CodigoCurso` `Course_Id` INT NOT NULL ,
CHANGE COLUMN `Nombre` `Course_Name` VARCHAR(30) NOT NULL ,
DROP COLUMN `FechaRealizacion`,
DROP COLUMN `Horario`;

# Renombre la columna “Costo realización” como "Costo efectivo", en la tabla Cursos económicos. 
		# restar el valor de ‘public_benefits’.
ALTER TABLE `amanel`.`cursos_economicos` 
CHANGE COLUMN `CostoRealizacion` `Cash_payment` INT NOT NULL;

UPDATE `amanel`.`cursos_economicos` SET `Cash_payment` = (44000 - public_benefits) WHERE (`Course_Id` = '1111');
UPDATE `amanel`.`cursos_economicos` SET `Cash_payment` = (88000 - public_benefits) WHERE (`Course_Id` = '1122');
UPDATE `amanel`.`cursos_economicos` SET `Cash_payment` = (88000 - public_benefits) WHERE (`Course_Id` = '1199');

#actualice 5 cursos y 3 profesores. 
UPDATE `amanel`.`capacitacion` SET `Horario` = '11:00:00' WHERE (`CodigoCurso` = '1188');
UPDATE `amanel`.`capacitacion` SET `Horario` = '11:00:00' WHERE (`CodigoCurso` = '2223');
UPDATE `amanel`.`capacitacion` SET `Horario` = '11:00:00' WHERE (`CodigoCurso` = '2211');
UPDATE `amanel`.`capacitacion` SET `Horario` = '11:00:00' WHERE (`CodigoCurso` = '1166');
UPDATE `amanel`.`capacitacion` SET `Horario` = '11:00:00' WHERE (`CodigoCurso` = '1177');

UPDATE `amanel`.`operadores` SET `Salario_x_curso` = '111000' WHERE (`RUN` = '17358762');
UPDATE `amanel`.`operadores` SET `Salario_x_curso` = '111000' WHERE (`RUN` = '18765283');
UPDATE `amanel`.`operadores` SET `Salario_x_curso` = '111000' WHERE (`RUN` = '19765432');

