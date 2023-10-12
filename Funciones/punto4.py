def multi_lista(lista):

    multiplicacion = 0
    
    for numero in lista:
        multiplicacion += numero
    return multiplicacion

lista_2 = [54, 1, 41, 17, 25]

resultado = multi_lista(lista_2)

print(f"El resultado es: {resultado}")