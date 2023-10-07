#Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. 

print ("Calcular el promedio de 5 numero")

numero_1 = float(input("Ingrese la primera nota: "))
numero_2 = float(input("Ingrese la segunda nota: "))
numero_3 = float(input("Ingrese la tercera nota: "))
numero_4 = float(input("Ingrese la cuarta nota: "))
numero_5 = float(input("Ingrese la quinta nota: "))

promedio = (numero_1 + numero_2 + numero_3 + numero_4 + numero_5) / 5

if promedio >= 3.0 and promedio <= 5.0:
    print(f" Su nota es {promedio} y usted aprobo. ")
elif promedio <= 3.0 and promedio >= 0.0:
    print(f" Su nota es {promedio} y ustde no aprobo")
else:
    print(" Las notas ingresadas estn mal escritas vuelvalo hacer. ")


