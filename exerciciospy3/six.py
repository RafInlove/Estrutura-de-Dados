# Escreva um programa que cria uma
# lista de strings e exibe a mais longa palavra da lista.
list = ['Paralelepípedo', 'Akuma no Mi', 'Beyblade', 'Garfo', 'Livro']

def getBigger(arr):
    maior = ""

    for i in arr:
        if len(i) > len(maior):
            maior = i
    return maior

print (getBigger(list))