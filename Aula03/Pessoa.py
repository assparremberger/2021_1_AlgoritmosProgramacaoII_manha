class Pessoa:

    def __init__(self, cod = None, name = None):
        self.codigo = cod
        self.nome = name

    def imprimir(self):
        print("Código: ", self.codigo)
        print("Nome: " , self.nome)
        