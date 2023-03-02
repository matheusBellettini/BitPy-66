# Definindo a função que retorna a sequência de Fibonacci
def fibonacci(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]

# Soma dos valores pares da sequência de Fibonacci
soma = sum([x for x in fibonacci(4000000) if x % 2 == 0])

# Imprimindo o resultado
print(soma)

