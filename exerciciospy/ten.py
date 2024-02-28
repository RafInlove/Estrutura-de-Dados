'''Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
computador e determinar o vencedor.'''
import random

pedra = 1
papel = 2
tesoura = 3

botInput = random.randint(1, 3)


print("Bem-vindo(a) ao jokenpô ! Vamos jogar")
print("Olha só:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")
print("Escolha com cuidado ok ? Vamos em lá !")
print("Jo...")
print("Ken...")
userInput = int(input("PO: "))

if botInput == pedra and userInput == tesoura:
    print("BOOO ! Eu escolhi pedra, tomou filho ! HAHAHAHAHA")
elif botInput == pedra and userInput == papel:
    print("DROGA ! Eu escolhi pedra, então acho que você ganhou....deu sorte !")
elif botInput == papel and userInput == tesoura:
    print("DROGA ! Eu escolhi papel, e você foi de tesoura né ? Me lasquei...")
elif botInput == papel and userInput == pedra:
    print("HAHA ! Eu escolhi papel, e você pedra. (trombone intensifies)")
elif botInput == tesoura and userInput == pedra:
    print("Puts...Escolhi tesoura....")
elif botInput == tesoura and userInput == papel:
    print("HEHEE ! Escolhi tesoura e cortei o seu papel !")
else:
    print("Bom, acho que foi epate. Vamos de novo !")
