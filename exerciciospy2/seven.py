'''Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
chamado “detalhes” que retorna uma string com as informações do carro.'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano
    
    def detalhes(self, marca, modelo, ano):
        return print("Marca: " ,marca, "\nModelo: " ,modelo, "\nAno: " ,ano )
    
c1 = Carro("Honda", "Civic", 2020)

c1.detalhes(c1.marca, c1.modelo, c1.ano)