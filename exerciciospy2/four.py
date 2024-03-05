'''Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
métodos “depositar” e “sacar” para manipular o saldo.'''

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, x):
        return self.saldo + x
    
    def sacar(self, x):
        return self.saldo - x
    
c1 = ContaBancaria(1500, "John")

c1.saldo = c1.depositar(25)
print(c1.saldo)

c1.saldo = c1.sacar(25)
print(c1.saldo)