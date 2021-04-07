class Produto():

    def __init__(self, nomeP = None, precoP = 0.0):
        self.nome = nomeP
        self.preco = precoP

    def cadastrar(self):
        print("O produto " , self.nome, " de preço ", self.preco, " foi cadastrado!")

    def alterarPreco(self, percentual):
        self.preco = self.preco + ( self.preco * percentual / 100)
