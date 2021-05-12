
arquivo = open("novo.txt", "w")
arquivo.write("Boa tarde")
arquivo.close()


arquivo = open("novo.txt", "a")
arquivo.write("Boa noite")
arquivo.close()

# Criando e escrevendo em um arquivo novo
arquivo = open("novo.txt", "w")
arquivo.write("Escrevendo no Arquivo")
arquivo.close()

# Lendo o arquivo
arquivo = open("novo.txt", "r")
print( arquivo.read())