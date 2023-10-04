cantidad = int(input("Ingrese la cantidad de productos: "))
valor_unitario = float(input("Ingrese el valor unitario de ls productos"))

valor_final = ( cantidad * valor_unitario) + ((cantidad * valor_unitario)*16)/100

print(f"El valor total de la compra es: {valor_final}")