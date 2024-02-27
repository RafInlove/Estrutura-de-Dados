# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.
def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibo():
    try:
        num = int(input("Digite um número para imprimir a sequência de Fibonacci até esse valor: "))
        if num < 0:
            print("Por favor, insira um número positivo.")
        else:
            fib_sequence = fibonacci(num)
            print("Sequência de Fibonacci até", num, ":")
            for fib in fib_sequence:
                print(fib, end=" ")
    except ValueError:
        print("Por favor, insira um número válido.")


fibo()


