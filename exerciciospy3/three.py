# Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da
# lista.
import random

list = []

for i in range(0, 10):
    list.append(random.randint(0, 10))

def soma(arr):
    total = 0
    for i in arr:
        total += i
    return total

print(f'A lista é: {list}')
print(f'A soma de todos os elementos da lista é: {soma(list)}')

