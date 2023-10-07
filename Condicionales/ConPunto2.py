print(" Informacion personal")

nombre = str(input(" Ingrese su nombre: "))
edad = int(input(" Ingrese su edad: "))

if edad >= 18 and edad <= 99:
    print(f" Hola, {nombre}, tu edad es {edad} y eres mayor de edad. ")
elif edad <=17 and edad >= 1:
    print(f" Hola, {nombre}, tu edad es {edad} y eres un menor de edad. ")
else:
    print(f" Hola, {nombre}, la edad colocoda es nula. ")    