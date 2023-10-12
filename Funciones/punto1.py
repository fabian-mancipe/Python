def encontrar_maximo(a, b, c):
    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    return maximo

numero1 = 105
numero2 = 56
numero3 = 810

maximo = encontrar_maximo(numero1, numero2, numero3)
print(f"El máximo de {numero1}, {numero2} y {numero3} es {maximo}")
