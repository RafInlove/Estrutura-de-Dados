# Faça um programa que leia uma lista de números e retorne a média dos números pares.
nList = [2, 5, 13, 10, 8, 1059, 73, 61, 90, 1]
parList = []


for i in (nList):
    if i%2 == 0:
        parList.append(i)

def parMedia():
    return sum(parList)/ len(parList)
    

print(f'Estes são todos os números da lista: {nList}')
print(f'Os números pares: {parList}')
print(f'E a média dos números pares: {parMedia()}')

            