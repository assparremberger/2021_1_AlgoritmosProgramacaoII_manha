carros =   "Uno", "Chevett", "Fusca", 25 , 3.7, True 
print( carros )

#carros[1] = "Toro"
print( carros[1] )

print("-----------------------------------------")

for car in carros:
    print( car )

print("-----------------------------------------")

print( carros[1:4] )

print( carros[2:] )

print( carros[-2] )

print( carros[-3:] )

print( carros[-3: -1] )

print("-----------------------------------------")

carros = "EcoSport", "Doblo", "Onix", "Ferrari"

print( sorted(carros) )

cars = sorted( carros )
print( cars )
cars[1] = "Fusca"
print( cars )

print("-----------------------------------------")

for index in range( len(carros) ) :
    print( "Posição ", index, " - Carro ",  carros[index] )

print("-----------------------------------------")

for index, nome in enumerate(carros):
    print( "Posição ", index, " - Carro ",  nome )


print("--------- Usando tuplas em funções --------")
def calcular( x , y):
    return x+y , x-y, x*y, x/y

print( calcular( 8, 4) )

nomes = ("Adalto", "João")
print( nomes )