# Escreva um programa que cria uma lista de números inteiros
# e exibe os números ímpares da lista.
import random

list = []
imparList = []

for i in range(0, 10):
    list.append(random.randint(0, 10))

def getImpar(arr):
    for i in arr:
        if i%2 != 0:
            imparList.append(i)

getImpar(list)

print("Esta é a lista padrão de números: ", list)
print("Estes são apenas os números ímpares da lista: ", imparList)