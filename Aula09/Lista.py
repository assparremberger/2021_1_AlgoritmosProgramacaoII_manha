from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, valor):
        # if self.tamanho > 0:
        if self.inicio:
            aux = self.inicio

            while( aux.proximo ) :
                aux = aux.proximo
            
            aux.proximo = No(valor)
        else: 
            self.inicio = No(valor)
        
        self.tamanho += 1
        self.imprimir()


    def imprimir(self):
        if self.inicio == None :
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while( aux ) :
                print( aux.dado )
                aux = aux.proximo
            
            print("Tamanho da Lista: ", self.tamanho)
            print("--------------------------")

    def excluir(self, valor):
        if self.tamanho == 0 :
            print("Lista Vazia")
        elif self.tamanho == 1 :
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho -= 1
            else:
                print("Valor não encontrado")
        else:
            tamAnterior = self.tamanho
            if self.inicio.dado == valor :
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            else:
                anterior = self.inicio
                aux = self.inicio.proximo
                x = 2
                while( aux != None ) :
                    if aux.dado == valor : 
                        anterior.proximo = aux.proximo
                        self.tamanho -= 1
                    else:
                        anterior = aux
                    aux = aux.proximo
                    

            if tamAnterior == self.tamanho :
                print("Valor não encontrado!")
        self.imprimir()