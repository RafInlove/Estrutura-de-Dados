'''Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
chamado “calcular_area” que retorna a área do retângulo.'''

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self, base, altura):
        return base*altura


r1 = Retangulo(0,0)

r1.base = int(input("Digite a medida da base: "))
r1.altura = int(input("Digite a medida da altura: "))

print("A área do triângulo é: ", r1.calcular_area(r1.base, r1.altura))