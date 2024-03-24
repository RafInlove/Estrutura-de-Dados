# Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista.

list = ['Donatello', 'Michelângelo', 'Leonardo', 'Raphael']

def ListLen(arr):
    contador = 0
    for i in arr:
        contador += 1
    return contador

print(ListLen(list))