def elementos_unicos(lista):

    conjunto_unico = set(lista)

    lista_unicos = list(conjunto_unico)
    return lista_unicos


mi_lista = int(input("Ingrese una lista de numero: "))
lista_sin_duplicados = elementos_unicos(mi_lista)

print("Lista original:", {mi_lista})
print("Lista con elementos únicos:", lista_sin_duplicados)
