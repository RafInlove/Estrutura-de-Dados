# Escreva um programa que cria uma lista de números inteiros
# e exibe os números pares da lista.
import random

list = []
parList = []

for i in range(0, 10):
    list.append(random.randint(0, 10))

def getPar(arr):
    for i in arr:
        if i%2 == 0:
            parList.append(i)

getPar(list)

print("Esta é a lista padrão de números: ", list)
print("Estes são apenas os números pares da lista: ", parList)