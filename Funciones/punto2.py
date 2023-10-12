def calcular_area(opcion):
    if opcion == "1":
        print("AREA DE UN CUADRADO")
        print(" ")
        numero = float(input("Ingrese el valor de uno de los lados del cuadrado: "))
        area_cuadrado = numero * numero
        print(f"El área del cuadrado es {area_cuadrado}")
        print(" ")
        
    elif opcion == "2":
        print("AREA DE UN RECTÁNGULO")
        print(" ")
        lado_a = float(input("Ingrese el lado A del rectángulo: "))
        lado_b = float(input("Ingrese el lado B del rectángulo: "))
        area_rectangulo = lado_a * lado_b 
        print(f"El área del rectángulo es {area_rectangulo}")
        print(" ")

    elif opcion == "3":
        print("AREA DE UN TRIÁNGULO")
        print(" ")
        base = float(input("Ingrese el valor de la base del triángulo: "))
        altura = float(input("Ingrese el valor de la altura del triángulo: "))
        area_triangulo = (base * altura) / 2
        print(f"El área del triángulo es {area_triangulo}")
        print(" ")

    elif opcion == "4":
        print("AREA DE UN CÍRCULO")
        print(" ")
        radio = float(input("Ingresar el radio del círculo: "))
        area_circulo = (radio * radio) * 3.14
        print(f"El área del círculo es {area_circulo}")
        print(" ")

    elif opcion == "5":
        print("AREA DE UN ROMBO")
        print(" ")
        diagonal_mayor = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese el valor de la diagonal menor del rombo: "))
        area_rombo = (diagonal_mayor * diagonal_menor) / 2
        print(f"El área del rombo es {area_rombo}")
        print(" ")

    elif opcion == "6":
        print("AREA DE UN TRAPECIO")
        print(" ")
        base_mayor = float(input("Ingrese el valor de la base mayor del trapecio: "))
        base_menor = float(input("Ingrese el valor de la base menor del trapecio: "))
        altura = float(input("Ingrese el valor de la altura del trapecio: "))
        area_trapecio = ((base_mayor + base_menor) * altura) / 2
        print(f"El área del trapecio es {area_trapecio}")
        print(" ")

    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

while True:
    print("Menu de Opciones:")
    print("1. Área de un cuadrado")
    print("2. Área de un rectángulo")
    print("3. Área de un triángulo")
    print("4. Área de un círculo")
    print("5. Área de un rombo")
    print("6. Área de un trapecio")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    print(" ")

    calcular_area(opcion)
