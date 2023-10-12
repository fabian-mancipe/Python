def contar_letras(cadena):
    mayusculas = 0
    minusculas = 0

    for letra in cadena:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1

    return mayusculas, minusculas


cadena = str(input("Ingrese un oracion: "))
mayusculas, minusculas = contar_letras(cadena)

print(f"Número de letras mayúsculas: {mayusculas}")
print(f"Número de letras minúsculas: {minusculas}")
