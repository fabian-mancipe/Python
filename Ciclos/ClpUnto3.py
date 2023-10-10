def fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def suma_fibonacci(n):
    return sum(fibonacci(n))


n = int(input("Ingrese la cantidad de términos de Fibonacci que desea mostrar: "))

fibonacci_sequence = fibonacci(n)

print(f"Los primeros {n} términos de Fibonacci son:")
for term in fibonacci_sequence:
    print(term)

suma = suma_fibonacci(n)
print(f"La suma de los primeros {n} términos de Fibonacci es: {suma}")
