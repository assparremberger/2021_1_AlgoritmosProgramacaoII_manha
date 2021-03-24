from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p1 = Pessoa(1, "João")
p1.imprimir()

pf = Fisica(2, "Maria", "111.222.333-44")
pf.imprimir()

pj = Juridica(3, "Mercado do João", "11.222.333")
pj.imprimir()
