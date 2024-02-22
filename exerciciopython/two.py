# Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

'''Pegando e armazenando número que o usuário digita em uma variável'''
n = int(input("Olá ! Me dê um número inteiro: "))

'''Se o número que o usuário digitou tiver o resto da divisão igual a 0,
então o número é par, se não, é ímpar.

o operador % é de divisão, porém não pega o resultado da divisão, e sim
o resto dela
'''
if n%2 == 0:
    print ("Este número é par !")
else:
    print("Este número é ímpar !")

'''Um número par, quando é dividido por dois, nunca sobra resto na divisão.
Porém, se o número for ímpar, sobram restos'''

