# Escreva um programa que cria uma
# lista de números inteiros e exibe a média dos números da lista.
import random

list = []

for i in range(0, 5):
    list.append(random.randint(0, 10))

def soma(arr):
    total = 0
    for i in arr:
        total += i
    return total

def media(arr, x):
    lenght = len(arr)
    result = soma(arr)

    return result/lenght

print(f'A lista é: {list}')
print(f'A soma de todos os elementos da lista é: {soma(list)}')
print(f'A média dos elementos da lista é: {media(list,soma(list))}')