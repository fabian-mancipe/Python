#Calcular la hipotenusa con el Teorema de Pitágoras.

numero_1 = float(input("Ingrese la medida del caateto 'a' del triangulo: " ))
numero_2 = float(input("Ingrese la medida del caateto 'b' del triangulo: " ))

cateto_a = numero_1 * numero_1 
cateto_b = numero_2 * numero_2 

hipotenusa = cateto_a + cateto_b 

print(f"La hipotenus del triangulo es: {hipotenusa}")