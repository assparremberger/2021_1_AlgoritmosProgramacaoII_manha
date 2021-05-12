import os

try:
    arquivo = open("dados2.txt", "r")
    os.remove( "dados2.txt" )
    print( "Arquivo excluído!")
except:
    print("Arquivo não existe")