from Produto import Produto

class Perecivel( Produto ):
    def __init__(self, nomePP = None , precoPP = 0.0,  temp = None):
        Produto.__init__(self, nomePP, precoPP)
        self.temperatura = temp

    def cadastrar(self):
        #Produto.cadastrar(self)
        #print("Temperatura máxima: " , self.temperatura)
        print("O produto " , self.nome, " de preço ", self.preco, " e temperatura máxima ", self.temperatura, " foi cadastrado!")

    def alterarPreco(self, percentual):
        percentual = percentual * 2
        Produto.alterarPreco(self, percentual)

