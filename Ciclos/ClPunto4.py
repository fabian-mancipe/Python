
suma = 0
contador = 0

for i in range(10):
    try:
        numero = float(input(f"Ingrese la secuencia de numeros: "))  
        suma += numero  
        contador += 1  
    except ValueError:
        print("Por favor, ingrese un número válido.")

if contador > 0:
    promedio = suma / contador
    print(f"La suma de los números es: {suma}")
    print(f"El promedio de los números es: {promedio}")
else:
    print("No se ingresaron números válidos para calcular la suma y el promedio.")
