def verificar_rango(numero, rango_minimo, rango_maximo):
    if numero >= rango_minimo and numero <= rango_maximo:
        return True
    else:
        return False


numero = int(input("ingrese un numero por favor: "))
rango_minimo = 1
rango_maximo = 99

if verificar_rango(numero, rango_minimo, rango_maximo):
    print(f"{numero} está dentro del rango ({rango_minimo}, {rango_maximo}).")
else:
    print(f"{numero} está fuera del rango ({rango_minimo}, {rango_maximo}).")
