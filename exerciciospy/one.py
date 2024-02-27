# Faça um programa que calcule a média de três números inseridos pelo usuário.
n1 = int(input('Digite um número: (1/3) '))
n2 = int(input('Digite um número: (2/3) '))
n3 = int (input('Digite um número: (3/3) '))

def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

print(media(n1,n2,n3))