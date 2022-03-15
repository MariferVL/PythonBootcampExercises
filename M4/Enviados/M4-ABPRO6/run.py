import poo


db_proveedores = {
    1: poo.Proveedor('Proveedor A', '1234', 'Proveedor A Ltda.', 'razon social caca A', 'Chile', 'Juridica'),
    2: poo.Proveedor('Proveedor B', '5678', 'Proveedor B Ltda.', 'razon social caca B', 'Peru', 'Juridica')
}

db_clientes = {
    1: poo.Cliente(1, "José", "Rua", "jose@gmail.com", "2020-10-01", 1000, 33),
    2: poo.Cliente(2, "Maria", "Lee", "maria@gmail.com", "2018-12-03", 2000, 43),
    3: poo.Cliente(3, "Kimberly", "Choriza", "kim@gmail.com", "2009-03-23", 3000, 23),
    4: poo.Cliente(4, "Tamara", "Neira", "tamara@gmail.com", "1980-12-22", 4000, 45),
    5: poo.Cliente(5, "Paula", "Ramirez", "paula@gmail.com", "1998-12-21", 5000, 88)
}
# def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto)
db_productos = {
    836942: poo.Producto(836942, 'zapatillas', 'calzado', db_proveedores[1].RUT, 35, 329586, 'blanco'),
    642264: poo.Producto(642264, 'polearas', 'ropa', 'china', 735, 3, 'rosa'),
    624426: poo.Producto(624426, 'zapatos', 'calzado', db_proveedores[2].RUT, 24, 735735, 'rojo'),
    264624: poo.Producto(264624, 'poleron', 'ropa', 'EU', 45, 4685732, 'verde'),
    624642: poo.Producto(624642, 'chaqueta', 'ropa', 'EU', 36, 753, 'azul'),
    624643: poo.Producto(624642, 'guantes', 'accesorio', 'EU', 753, 735, 'naranja')
}

# (self, run, nombre, apellido, seccion)
db_vendedores = {
    15666777: poo.Vendedor(15666777, 'Juan', 'Perez', 1, '2020-10-01'),
    15222777: poo.Vendedor(15222777, 'Pedro', 'Gonzalez', 2, '2018-12-03'),
}

# reporte estadistico del inventario
poo.reporte_estadistica_productos(db_productos)

db_clientes[1].get_saldo()

db_vendedores[15666777].vender(id_venta=1,
                            cliente=db_clientes[1],
                            productos=[db_productos[642264]],
                            cantidad=[3]
                            )
print("despues de la venta_")
poo.reporte_estadistica_productos(db_productos)

db_clientes[1].get_saldo()
