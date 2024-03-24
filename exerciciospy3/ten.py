# Escreva um programa que cria uma lista de números inteiros e remove todos os números
# repetidos, exibindo a lista resultante.
import random

numList = []
noRepeatList = []

def construirLista(arr):
    for i in range(0, 5):
        arr.append(random.randint(0, 10))

construirLista(numList)

for i in numList:
    if i not in noRepeatList:
        noRepeatList.append(i)

print("Esta é a lista: ", numList)
print("Estes é a lista sem repetições: ", noRepeatList)