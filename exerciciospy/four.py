# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
# esse número.
userInput = int(input("Me dê um número inteiro: "))
nums = []

def findPar(userInput):
    for i in range (userInput + 1):
        if i%2 == 0:
            nums.append(i)

findPar(userInput)
print(f'{nums}, são pares.')