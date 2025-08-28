"""
• Classe base ContaBancaria: titular, saldo, depositar, sacar.
• ContaCorrente: tem taxa de manutenção mensal.
• ContaPoupanca: tem rendimento mensal fixo (ex: 0.5%).
• Método para aplicar manutenção ou rendimento."""

class ContaCorrente:
    def __init__(self,nome,saldo):
        self.__nome = nome
        self.__saldo = saldo
    
    def get_status_conta(self):
        return f"{self.__nome} tem saldo: {self.__saldo}"
    

    def depositar(self,deposito):
        if deposito > 0:
            self.__saldo += deposito
        else:
            print("Valor invalido")
    
    def sacar(self,saque):
        if saque > 0:
            self.__saldo -= saque
        else:
            print("Valor invalido")

class ContaPoupanca:
    def __init__(self,nome,saldo):
        self.__nome = nome
        self.__saldo = saldo

    def depositar(self,deposito):
        if deposito > 0:
            self.__saldo += deposito
        else:
            print("Valor invalido")
    
    def sacar(self,saque):
        if saque > 0:
            self.__saldo -= saque
        else:
            print("Valor invalido")
    
    def status_rendimento(self,rendimento):
        return f"{self.__saldo + (self.__saldo * rendimento)}"
    
    def get_status_conta(self):
          return f"{self.__nome} tem saldo: {self.__saldo}"


############
ednei = ContaCorrente("ednei",1000)
ednei.get_status_conta()

    

