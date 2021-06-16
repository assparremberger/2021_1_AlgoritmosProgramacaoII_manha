from Pilha import Pilha

pilha = Pilha()

pilha.imprimir()

pilha.adicionar("Computador")
pilha.imprimir()

pilha.adicionar("Notebook")
pilha.imprimir()

pilha.empilhar("Tablet")

pilha.empilhar("Smartphone")

pilha.imprimir()

print("---- Removendo ----")

pilha.remover()
pilha.adicionar("Relógio")
pilha.imprimir()

pilha.remover()
pilha.remover()
pilha.remover()
pilha.remover()