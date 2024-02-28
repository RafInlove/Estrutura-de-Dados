# Faça um programa que determine se um número é primo ou não.
userInput = (int(input("Me dê um número, e direi se ele é primo ou não: ")))

if userInput%2 == 0 or userInput%3 == 0 or userInput%5 == 0:
    print("Não é primo.")
else:
    print("É primo !")
