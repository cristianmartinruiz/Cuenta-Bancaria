class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta #atributo protegido
        self.__saldo = saldo #atributo privado

    def get_saldo(self):
        return self.__saldo
    
    def depositar (self, monto):
        self.__saldo += monto

    def retirar (self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto 
        else:
            print ("Saldo insuficiente")

# Modo de uso 
cuenta = CuentaBancaria(123456789, 1500)
print (cuenta._numero_cuenta)

# obtener saldo
valor = cuenta.get_saldo()
print (valor)

# utilizar metodos publicos
cuenta.depositar(500)
cuenta.retirar (300)
print (cuenta.get_saldo())