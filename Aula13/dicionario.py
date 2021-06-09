pessoa = { "nome" : "Maria" , "idade" : 25 , "altura" : 1.75 , "temFilhos" : False }

print( pessoa )

print( "Nome: " , pessoa["nome"] )

pessoa["idade"] += 2 

print( pessoa )

# print( pessoa[1] )

del pessoa["idade"]
print( pessoa )

pessoa["email"] = "m@m.com"

print( pessoa )

print("-------------------------------------")

carro01 = { "modelo": "Uno" , "ano": 2004}
carro02 = { "modelo": "Doblo" , "ano": 2006}

frota = carro01, carro02 

print( frota )

print( frota[1]["modelo"] )

frota[1]["ano"] = 2010

print( frota )