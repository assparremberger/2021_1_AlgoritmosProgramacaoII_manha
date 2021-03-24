from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, codFisica, nameFisica, cpf):
        Pessoa.__init__(self, codFisica, nameFisica)
        self.cpf = cpf

    def imprimir(self):
        Pessoa.imprimir(self)
        print("CPF: " , self.cpf)