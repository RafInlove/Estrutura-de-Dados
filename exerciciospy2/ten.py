'''Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
do funcionário.'''

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario 
        self.cargo = cargo
    
    def aumentar_salario(self, x, salario):
        return salario * x
    
    def calcular_porcentagem(self, x):
        return x / 100
    
f1 = Funcionario("Manoel", 1824, "Auxiliar de Produção")

print("O salário atual de", f1.nome, "é", f1.salario)

aumento = int(input("Digite o aumento: "))
aumento = f1.calcular_porcentagem(aumento)

print("O salário atual de ", f1.nome, "é ", f1.salario + f1.aumentar_salario(aumento, f1.salario))