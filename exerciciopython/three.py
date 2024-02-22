# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
# esse número.

'''Priando listas para guardar todos os números e os números pares respectivamente'''
numberlist = []
parlist = []
'''Pegando número do usuário e armazenando na variável'''
usernumber = int(input("Olá ! Me dê um número inteiro: "))

'''Enquanto o número que o usuário digitou for maior que 1, subtraia 1 do mesmo,
depois, adicione o resultado a lista de numeros pares'''
while usernumber > 1:
    usernumber -=1
    numberlist.append(usernumber)
'''Verificando se o número é par, e se for, adicionando a lista de números pares

    Para cada item na lista de números: se o item tiver o resto da divisão igual a 0,
    então adicione ele a lista de números pares'''
for i in numberlist:
    if i%2 == 0:
        parlist.append(i)

print("Todos os números pares até 0 antecessores a este número são:", parlist)

