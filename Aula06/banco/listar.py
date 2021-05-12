import mysql.connector

conn = mysql.connector.connect(host='localhost', database = 'pi2_loja_2021_1', user='root', password='')

if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM produto" )
    result = cursor.fetchall()

    for produto in result:
        texto = str( produto[0] ) + ": " + produto[1] + " | R$ " + str( produto[2] )
        print( texto )
        print( "-----------------------------------------")

    cursor.close()
    conn.close()