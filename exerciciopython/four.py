# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

'''Criando uma lista vazia e uma variável'''
numberlist = []
usern = 0

'''Funções que retornam o maior e menor valor dentro de uma lista'''
def maiorN():
    return (max(int(i) for i in numberlist))

def menorN():
    return (min(int(i) for i in numberlist))
'''Para cada item em até 3 itens, peça um número do usuário, e o adicione
à lista de números'''
for i in range(3):
    usern = int(input("Digite um número: "))
    numberlist.append(usern)
'''output:
PS: Lembra sempre de chamar a função'''
print("O maior número entre estes é o:",maiorN())
print("E o menor é o:",menorN())

