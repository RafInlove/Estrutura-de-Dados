# Escreva um programa que cria duas listas de números inteiros
# e exibe os números que estão presentes em ambas as listas.
import random

numList = []
numList2 = []
allNumList = []

def construirLista(arr):
    for i in range(0, 5):
        arr.append(random.randint(0, 10))

def fundirLista(arrTarget, arr, arr2):
    arrTarget.append(arr)
    arrTarget.append(arr2)

construirLista(numList)
construirLista(numList2)
fundirLista(allNumList, numList, numList2)

print("Esta é a lista 1: ", numList)
print("Esta é a lista 2: ", numList2)
print("Estes são todos os números das duas listas: ", allNumList)