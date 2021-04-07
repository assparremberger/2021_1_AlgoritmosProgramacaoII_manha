from Conta import Conta

c1 = Conta()
c1.imprimirSaldo()

c1.depositar(10.5)
c1.imprimirSaldo()

c1.sacar( 5 )
c1.imprimirSaldo()

c1.__saldo = 20
c1.imprimirSaldo()

c1._limite = 500.0
print( "Limite: " , c1._limite)

print("O saldo é aaa: ", c1.__saldo)
c1.imprimirSaldo()

c1.setSaldo( 52.6 )
print( "Saldo: ", c1.getSaldo() )

c1.imprimirSaldo()