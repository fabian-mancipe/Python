
print ("SALARIO DEL TRABAJADOR")

salario_dia = float(input("Ingrese el salario del trabajador: "))
dias_trabajados = int(input("Ingrese los dias laboraddos del trabajador: "))

resultado = salario_dia * dias_trabajados
pension_salud = resultado - (resultado * 0.25)


print (f"El sueldo que resibe el empleado es: {pension_salud}")