#Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio).

while True:
    print("Menu de Opciones:")
    print("1. area de un cuadrado")
    print("2. area de un rectangulo")
    print("3. area de un triangulo")
    print("4. area de un circulo")
    print("5. area de un rombo")
    print("6. area de un trapecio")
    print("7. Salir")
    

    opcion = input("Seleccione una opción: ")
    print(" ")

    if opcion == "1":
        
        print(" AREA DE UN CUADRADO")
        print(" ")
        numero = float(input(" Ingrese el valor de uno de los lados del cuadrado: "))

        area_cuadrado = numero * numero

        print(f" El area del cuadrado es {area_cuadrado} ")
        print(" ")
        
    elif opcion == "2":
        print(" AREA DE UN RECTANGULO")
        print(" ")
        lado_a = float(input("Ingrese el lado A del recangulo: "))
        lado_b = float(input("Ingrese el lado B del recangulo: "))

        area_rectangulo = lado_a * lado_b 

        print(f" El area del rectangulo es {area_rectangulo} ")
        print(" ")

    elif opcion == "3":
        print(" AREA DE UN TRIANGULO")
        print(" ")

        base = float(input("Ingrese el valor de la base del triangulo: "))
        altura = float(input("Ingrese el valor de la altura del triagulo: "))

        area_triangulo = (base * altura)/2

        print(f" El area del triangulo es {area_triangulo} ")
        print(" ")

    elif opcion == "4":
        print(" AREA DE UN CIRCULO")
        print(" ")

        radio = float(input(" Ingresar el el radio que tiene el circulo: "))
        
        area_circulo = (radio * radio) * 3.14

        print(f" El area del circulo es {area_circulo} ")
        print(" ")

    elif opcion == "5":
        print(" AREA DE UN ROMBO")
        print(" ")

        diagonal_mayor = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese el valor de la diagonal menor del rombo: "))

        area_rombo = (diagonal_mayor * diagonal_menor)/2

        print(f" El area del rombo es {area_rombo} ")
        print(" ")

    elif opcion == "6":
        print(" AREA DE UN TRAPECIO")
        print(" ")

        base_mayor = float(input("Ingrese el valor de la base mayor del trapecio: "))
        base_menor = float(input("Ingrese el valor de la base menor del trapecio: "))
        altura = float(input("Ingrese el valor de la altura del trapecio: "))

        area_trapecio = ((base_mayor + base_menor) * altura)/2

        print(f" El area del trapecio es {area_trapecio} ")
        print(" ")

    elif opcion == "7":
        print("Saliendo del programa. ¡LOS VIDRIOS!")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
