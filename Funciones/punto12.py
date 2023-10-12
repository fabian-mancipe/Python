def palindromo(palabra):

    palabra = palabra.replace(" ", "").lower()
    

    return palabra == palabra[::-1]

palabra = str(input(" Por favor, ingrese una palabra: "))
if palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

    
