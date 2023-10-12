def invertir(cadena):

    cadena_invertida = cadena[::-1]
    return cadena_invertida

cadena = "ElPerroEnUnaCicla5643"


resultado = invertir(cadena)

print(f"La palabra {cadena} al invertirse queda asi: {resultado}")
