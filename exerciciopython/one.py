# Faça um programa que calcule a média de três números inseridos pelo usuário.

''' Pegando e armazenando os números que o usuário digita em três variáveis'''
n1 = int(input("Olá ! Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite apenas mais um número: "))

'''Função criada pra calcular a média, recebe como parâmetro os as três variáveis
que contém os valores digitados pelo usuário, soma todas e divide por 3 (quantidade)'''
def calcularmedia(n1,n2,n3):
    return (n1 + n2 + n3) / 3

'''output: 
PS: lembra sempre de chamar a função'''
print("A média destes números é:", calcularmedia(n1,n2,n3))
