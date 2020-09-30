listaRegistro = []
print("Ingrese el numero de clientes que desee")
clientes = 0
NumeroDeClientes = float(input("Numero de Clientes"))
TotalCostos = 0

while NumeroDeClientes > clientes:
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = float(input("Costo ($0.00): "))

    registro = dict(cliente=cliente, producto=producto, costo=costo)

    listaRegistro.append(registro)
    TotalCostos = costo + TotalCostos
    clientes += 1
for registro in listaRegistro:
    print(registro)
    print("El Total de los Costos hasta el momento es: ")
    print(TotalCostos)
