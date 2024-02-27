# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
# esse número.

userInput = int(input("Me dê um número inteiro: "))
arr = []

arr.append(userInput)

def catchNs():
    while userInput > 0:
        userInput -1
        return userInput
    
while userInput > 0:
    arr.append(catchNs())


print(arr)
