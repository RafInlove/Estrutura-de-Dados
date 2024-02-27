# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
# número.
def fatorar():
    userInput = int(input("Me de um número inteiro positivo: "))
    fat = 1
    i = 2
    
    while i <= userInput:
        fat = fat*i
        i = i + 1

    print("O fatorial de %d é" %userInput, fat)

fatorar()