altura = int(input("Ingresa la altura del triángulo: "))

for i in range(1, altura + 1):
    print("*" * i)


for i in range(altura - 1, 0, -1):
    print("*" * i)
