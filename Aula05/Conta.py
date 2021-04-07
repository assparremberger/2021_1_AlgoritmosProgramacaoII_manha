class Conta:

    def __init__(self):
        self.__saldo = 0.0
        self._limite = 1000.0

    def __descontarTarifa(self):
        self.__saldo -= 1.99

    def depositar(self, valor):
        self.__saldo += valor
        self.__descontarTarifa()

    def sacar(self, valor):
        self.__saldo -= valor
        self.__descontarTarifa()
    
    def imprimirSaldo(self):
        print("O saldo é: ", self.__saldo)

    def getSaldo(self):
        admin = True
        if admin :
            return self.__saldo

    def setSaldo(self, valor):
        admin = True
        if admin :
            self.__saldo = valor