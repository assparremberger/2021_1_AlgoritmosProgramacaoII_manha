from No import No

#Classe Lista para duplamente encadeada

class Lista:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def adicionarNoInicio( self, valor ) :
        no = No( valor )
        if self.tamanho == 0 :
            self.primeiro = no
            self.ultimo = no
        else:
            aux = self.primeiro
            no.proximo = aux
            aux.anterior = no
            self.primeiro = no
        self.tamanho += 1

    def adicionarNoFim( self, valor ) :
        no = No( valor )
        if self.tamanho == 0 :
            self.primeiro = no
            self.ultimo = no
        else:
            aux = self.ultimo
            no.anterior = aux
            aux.proximo = no
            self.ultimo = no
        self.tamanho += 1

    def imprimir(self):
        if self.tamanho == 0:
            print( "Lista Duplamente Encadeada vazia!")
        else:
            texto = ""
            aux = self.primeiro
            while( aux ) :
                texto += " --> " + str( aux.dado ) 
                aux = aux.proximo
            print( texto )
            print( "Tamanho: " + str( self.tamanho ) )

    def imprimirReverso(self):
        if self.tamanho == 0:
            print( "Lista Duplamente Encadeada vazia!")
        else:
            texto = ""
            aux = self.ultimo
            while( aux ) :
                texto += " <-- " + str( aux.dado ) 
                aux = aux.anterior
            print( texto )
            print( "Tamanho: " + str( self.tamanho ) )

    def removerNoInicio(self):
        if self.tamanho == 0:
            print( "Lista Duplamente Encadeada vazia!")
        elif self.tamanho == 1: 
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0   
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
            self.tamanho -= 1
        
    def removerNoFim(self):
        if self.tamanho == 0:
            print( "Lista Duplamente Encadeada vazia!")
        elif self.tamanho == 1: 
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0   
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
            self.tamanho -= 1