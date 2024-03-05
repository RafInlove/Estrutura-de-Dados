'''Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
“calcular_media” que retorna a média das notas do aluno.'''

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome 
        self.notas = notas
    
    def calcular_media(self, notas):
        return sum(notas) / len(notas)
    
a1 = Aluno ("José", [8, 10, 9, 8])

print(a1.calcular_media([8, 10, 9, 8]))
