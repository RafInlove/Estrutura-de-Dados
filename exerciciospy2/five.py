'''Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
chamado “falar” que imprime uma mensagem com o nome da pessoa.'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self, nome):
        return print("Olá ! Meu nome é "+nome)
    
p1 = Pessoa("Rogério", 29)

p1.falar(p1.nome)