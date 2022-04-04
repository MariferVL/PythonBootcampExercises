#D. Identifique cual es el salario mínimo entre vendedores.
SELECT min(salario) from vendedor;

#E. Identifique cual es el salario máximo entre vendedores.
SELECT max(salario) from vendedor;

#F. Súmele el salario mínimo identificado al salario de todos los vendedores.
SET SQL_SAFE_UPDATES = 0;
UPDATE vendedor SET salario = salario + (SELECT MIN(salario));
SELECT * FROM vendedor;

#G. Elimine el producto más caro del inventario.}
SET SQL_SAFE_UPDATES = 0;
SELECT * FROM productos;
DELETE FROM productos ORDER BY Precio DESC LIMIT 1;
SELECT * FROM productos;

#H. Cree una tabla que contenga solo los clientes que han pagado más que el promedio.     “clientespremium”
SELECT * FROM clientes;
CREATE TABLE clientespremium AS (SELECT * FROM clientes WHERE (TotalPagado > (SELECT AVG(TotalPagado) FROM clientes)));
SELECT * FROM clientespremium;

#I. Actualice los datos de tres productos.
UPDATE `telovendo`.`productos` SET `Precio` = '234234342' WHERE (`SKU` = '1012');
UPDATE `telovendo`.`productos` SET `Precio` = '234234234' WHERE (`SKU` = '1013');
UPDATE `telovendo`.`productos` SET `Precio` = '434432324234' WHERE (`SKU` = '1014');

#J. Actualice los datos de tres vendedores.
UPDATE `telovendo`.`vendedor` SET `salario` = '7050' WHERE (`Run` = '8365753');
UPDATE `telovendo`.`vendedor` SET `salario` = '40746' WHERE (`Run` = '1645753');
UPDATE `telovendo`.`vendedor` SET `salario` = '7200' WHERE (`Run` = '1445753');


#K. Actualice los datos de 1 cliente.
UPDATE `telovendo`.`clientes` SET `TotalPagado` = '76023423' WHERE (`idclientes` = '13902911');

#L. Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio.
SELECT * from vendedor;
SELECT NombreVendedor, ApellidosVendedor FROM vendedor WHERE (salario > (SELECT AVG(salario) FROM vendedor));

#M. Indique cuál es el cliente con mayor gasto.
SELECT * from clientes;
SELECT * FROM clientes WHERE (TotalPagado = (SELECT MAX(TotalPagado) FROM clientes));
