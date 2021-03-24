from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, codigo, nome, cnpj):
        Pessoa.__init__(self, codigo, nome)
        self.cnpj = cnpj

    def imprimir(self):
        Pessoa.imprimir(self)
        print("CNPJ: " , self.cnpj)