
#Crear la estructura de la base de datos.
CREATE SCHEMA `db1`;
USE db1;

#Crear usuario con privilegios para crear, eliminar y modificar tablas, insertar registros.
CREATE USER 'admin_tlv'@'localhost' IDENTIFIED BY '1234';
GRANT ALL ON db1.* TO 'admin_tlv'@'localhost';

#Crear tabla clientes:
		#solo 5 para probar la nueva base de datos. 
        # nombre, apellido, dirección (solo pueden ingresar una)
CREATE TABLE `db1`.`cliente` (
  `idCliente` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `dirección` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`));
  
INSERT INTO `db1`.`cliente` (`idCliente`, `nombre`, `apellido`, `dirección`) 
VALUES ('1', 'Juan', 'Perez', 'Calle camaron 123'),
		('2', 'Pedro ', 'Casas', 'Calle Langosta 234'),
		('3', 'Julia', 'Meza', 'Calle Jaiba 345'),
		('4', 'Marcia', 'Blanco', 'Calle ALmeja 456'),
		('5', 'Luis', 'Plaza', 'Calle Ostion 567'),
		('6', 'Pablo', 'Marmol', 'Calle Centolla 678'),
		('7', 'Bilma', 'Lopez', 'Calle Locos 789');

 # Crear tabla Proveedor: 
		#nombre del representante legal, 
        #su nombre corporativo, cliente
        #al menos dos teléfonos de contacto (y el nombre de quien recibe las llamadas),
        #la categoría de sus productos (solo nos pueden indicar una categoría) y 
        #un correo electrónico para enviar la factura.
		#Agregue 5 proveedores a la base de datos. 
  
CREATE TABLE `db1`.`proveedor` (
  `idProveedor` INT NOT NULL auto_increment,
  `categoria` VARCHAR(15) NOT NULL,
  `nombre_corporativo` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefono1` VARCHAR(12) NOT NULL,
  `nombre1` VARCHAR(22) NOT NULL,
  `telefono2` VARCHAR(12) NOT NULL,
  `nombre2` VARCHAR(22) NOT NULL,
  `telefono3` VARCHAR(12) NULL,
  `nombre3` VARCHAR(22) NULL,
  PRIMARY KEY (`idProveedor`));

#Cambiar el default del auto_increment para tener id más distintivos entre tablas.
ALTER TABLE proveedor auto_increment= 100;
  
INSERT INTO `db1`.`proveedor` ( `categoria`, `nombre_corporativo`, `email`, `telefono1`,`nombre1`, `telefono2`,`nombre2`,`telefono3`,`nombre3`) 
VALUES ('Audio', 'Caca Corp.', 'hola@caca.com','956987423', 'Pedro Capó','956987423','Gato Alquinta', null, null ),
		( 'Audiovisual', 'Umbrela Corp.','hola@umbrela.com', '954786325','Adele Blue' ,'954786325', 'Denise R.', null, null),
		('Cocina', 'Ratatuill SA.','hola@rata.com', '954129856','Cami Gallardo', '954129856', 'Zoe Gotusso','954129856', 'Fran V.' ),
		('Computación', 'Tesla SA.', 'hola@tesla.com','952367458','John Lennon' ,'952367458','Lily Allen' ,'952367458', 'Bruno Mars' ),
		('Computación', 'Edison SA.','hola@edi.com','954128569','Violeta Parra', '954128569', 'El Kuelgue','954128569', 'Ed Sheeran');

#Productos:
		#Ingrese 10 productos y su 
        # respectivo stock.
		# precio, su categoría, proveedor y color. 
        #Los productos pueden tener muchos proveedores. 
   
CREATE TABLE `db1`.`producto` (
  `idProducto` INT NOT NULL AUTO_INCREMENT,
  `nombre_producto` VARCHAR(75) NOT NULL,
  `precio` INT NOT NULL,
  `categoria` VARCHAR(45) NOT NULL,
  `color` VARCHAR(45) NULL,
  `stock` INT NOT NULL,
  `fk_idproveedor` INT NOT NULL,
  PRIMARY KEY (`idProducto`),
  INDEX `idProveedor_idx` (`fk_idproveedor` ASC) VISIBLE,
  CONSTRAINT `idProveedor`
  FOREIGN KEY (`fk_idproveedor`)
  REFERENCES `db1`.`proveedor` (`idProveedor`)
  ON DELETE CASCADE
  ON UPDATE CASCADE);
  
  ALTER TABLE producto auto_increment= 1000;
  
  INSERT INTO `db1`.`producto` (`precio`, `fk_idproveedor`, `categoria`, `color`, `stock`, `nombre_producto`) 
  VALUES ('18000', '100', 'Audio', 'Negro', '65', 'Audifonos'),
		('32000', '100', 'Audio', 'Negro', '18', 'Microfono'),
		('85000', '102', 'Electrodomésticos', 'Blanco', '12', 'Microondas'),
		( '18000', '102', 'Electrodomésticos', 'Rojo', '26', 'Hervidor'),
		( '150000', '101', 'TV', 'Blanco', '8', 'Televisor'),
		( '80000', '103', 'Computación', 'Blanco', '32', 'Mouse'),
		('150000', '100', 'Audio', 'Azul', '24', 'Parlantes'),
		('25000', '103', 'Computación', 'Azul', '68', 'Teclado'),
		( '89000', '104', 'Computación', 'Rojo', '14', 'Impresora'),
		('55000', '101', 'Audio', 'Negro', '18', 'Soundbar');
  
  #Tabla extra implementada para facilitar acceso a la información de venta.
  CREATE TABLE `db1`.`historial_compra` (
  `idcompra` INT NOT NULL AUTO_INCREMENT,
  `fechacompra` DATE NOT NULL,
  `saldo` INT NULL,
  `valor` INT NOT NULL,
  `fk_idcliente` INT NOT NULL,
  `fk_idproducto` INT NOT NULL,
  PRIMARY KEY (`idcompra`),
  INDEX `idproducto_idx` (`fk_idproducto` ASC) VISIBLE,
  INDEX `idcliente_idx` (`fk_idcliente` ASC) VISIBLE,
  CONSTRAINT `idproducto`
  FOREIGN KEY (`fk_idproducto`)
  REFERENCES `db1`.`producto` (`idProducto`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT `idcliente`
  FOREIGN KEY (`fk_idcliente`)
  REFERENCES `db1`.`cliente` (`idCliente`)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

 ALTER TABLE historial_compra auto_increment= 10000;

##Realizar consultas SQL que indiquen:

#Cuál es la categoría de productos que más se repite. 
#Query para 1 o más coincidencias.
SELECT categoria, count(categoria) as "Productos por categoría" from producto
group by categoria
having count(*)=
(SELECT count(categoria) from producto
group by categoria
order by categoria asc
limit 1);  

# Cuáles son los productos con mayor stock. 
#Query para 1 o más coincidencias.
SELECT nombre_producto as "Producto con mayor Stock", stock FROM producto WHERE(stock = (SELECT max(stock) FROM producto));            

# Qué color de producto es más común en nuestra tienda.
SELECT color, count(color) AS "Color mas común" FROM producto
GROUP BY color
HAVING count(*)=
(SELECT tabla_temp.col_aux FROM  
(SELECT COUNT(color) AS col_aux , color
FROM producto
GROUP BY color
ORDER BY count(color) DESC LIMIT 1)tabla_temp);  
          
# Cuál o cuáles son los proveedores con menor stock de productos.
Select nombre_corporativo, sum(stock) as "Stock Total" 
from producto, proveedor
where fk_idproveedor = idproveedor  
group by fk_idproveedor 
order by "Stock Total"  ASC;


#Cambien la categoría de productos más popular por ‘Electrónica y computación’.

# Categoría más vendida(menor stock)= TV
Select categoria, sum(stock) as stock_total 
from producto
group by categoria 
order by stock_total  DESC;

UPDATE `db1`.`producto` SET `categoria` = 'Electrónica y computación' 
WHERE (`idProducto` = '1014');
