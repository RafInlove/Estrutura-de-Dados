# Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista.
import random

list = []

for i in range(0, 10):
    list.append(random.randint(0, 10))

def getMax(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

print(list)
print(getMax(list))

