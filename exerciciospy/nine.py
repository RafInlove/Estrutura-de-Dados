# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que
# começam com a letra 'A'.

list = ['Angélica', 'Mathew', 'Ana', 'Rodolfo', 'Christopher', 'Amanda', 'Gordon', 'Viktor']
aList = []

for i in list:
    if i.startswith('A'):
        aList.append(i)


print(f'Esta é a lista de nomes: {list}')
print (f'E esta é a lista de nomes que começam com a letra A: {aList}')