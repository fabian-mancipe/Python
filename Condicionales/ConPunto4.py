
numero1 = int(input(" Ingrese el numero: "))
numero2 = int(input(" Ingrese el numero: "))

if numero1 < numero2:
    mayor = numero2
    menor = numero1
elif numero1 > numero2:
    mayor = numero1
    menor = numero2
else: 
    print(" los dos numeros son numeros son iguales. ")

if "mayor" in locals() and "menor" in locals():
    print(f" El numero mayor es {mayor} y el numero menor es {menor}. ")
    