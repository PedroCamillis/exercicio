def fibo(n):
    a, b = 0, 1
    
    if n == 0 or n == 1:
        return True

    while b < n:
        a, b = b, a + b

    if b == n:
        return True
    else:
        return False

numero = int(input("Informe um número: "))

if fibo(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
