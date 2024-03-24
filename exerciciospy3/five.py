# Escreva um programa que cria uma lista de palavras e exibe a quantidade de palavras que começam
# com a letra 'A'.
list = ['Rogério', 'Amanda', 'Angela', 'Alanda', 'Marques', 'André', 'Romeu']
aList = []

def filtrar(arr):
    for i in arr:
        if  i[0] == 'A' or i[0] == 'a':
            aList.append(i)

filtrar(list)

print(f'A lista de nomes é: {list}')
print(f'Desta lista, os nomes que começam com a letra "A" são: {aList}')