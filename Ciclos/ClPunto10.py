altura = int(input("Ingresa la altura para formar la Z: "))

for i in range(altura):
    if i == 0 or i == altura - 1:
        print("*" * altura)  
    else:

        for j in range(altura - i - 1):
            print(" ", end="")
        print("*") 
