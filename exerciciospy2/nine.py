'''Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
método chamado “calcular_perimetro” que retorna o perímetro do triângulo.'''

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1 
        self.lado2 = lado2 
        self.lado3 = lado3
    
    def calcular_perimetro(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    
t1 = Triangulo(5, 9, 5)

print(t1.calcular_perimetro(t1.lado1, t1.lado2, t1.lado3))