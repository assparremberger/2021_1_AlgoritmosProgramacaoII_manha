from Lista import Lista

lista = Lista()
lista.imprimir()
lista.adicionarNoInicio( 10 )
lista.adicionarNoInicio( 5 )
lista.adicionarNoFim( 15 )
lista.adicionarNoFim( 20 )
lista.adicionarNoInicio( 1 )
lista.imprimir()
lista.imprimirReverso()

print("----------------")

lista.removerNoInicio()
lista.imprimir()
lista.removerNoFim()
lista.imprimir()
lista.removerNoInicio()
lista.imprimir()
lista.removerNoFim()
lista.imprimir()
lista.removerNoFim()
lista.imprimir()