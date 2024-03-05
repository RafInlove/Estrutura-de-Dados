'''Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
“calcular_area” que retorna a área do círculo.'''
class Circulo:
    def __init__ (self, raio):
        self.raio = raio

    def calcular_area(self, raio):
        return 3.14 * raio ** 2

c1 = Circulo(raio = 0)

c1.raio = int(input("Digite o raio do círculo: "))

resposta = c1.calcular_area(c1.raio) 

print("A área deste círculo é: ", resposta)