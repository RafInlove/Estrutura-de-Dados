# Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.
userInput = int(input("Digite um número inteiro: "))

def define(userInput):
    if userInput%2 == 0:
        return print("Esse número é par !")
    else:
        return print ("Esse número é ímpar")
    
define(userInput)