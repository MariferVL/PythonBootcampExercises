import poo

client = poo.Cliente(1, "José", "Rua", "123123", 1000, 2121212121212)
product = poo.Producto(1, "Leche", "Leche", "Colun", 11, 10)

client.add_saldo(1212)
saldo = client.get_saldo()
print(saldo)