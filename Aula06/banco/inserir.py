# encoding: utf-8

import mysql.connector

conn = mysql.connector.connect(host='localhost', database = 'pi2_loja_2021_1', user='root', password='')

if conn.is_connected():
    nome = str( input( "Digite o nome do produto: ") )
    preco = str( input("Digite o preço: ") )
    preco = preco.replace( "," , ".")

    query = "INSERT INTO produto (nome, preco, codCategoria) VALUES ( "
    query += " '" + nome + "' , " + preco + " , 1 ) "

    cursor = conn.cursor()
    cursor.execute( query )
    conn.commit()

    cursor.close()
    conn.close()

