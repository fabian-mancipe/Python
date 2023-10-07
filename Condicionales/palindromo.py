
palindromo = str(input(" Ingrese la frase: "))
palindromo = palindromo.lower()
palindromo = palindromo.replace(" ", "")

invertida = palindromo[::-1]

if palindromo == invertida:
    print(F"La frase {palindromo} es un palindromo. ")
else:
    print(F" La frase {palindromo} no es un palindromo")
