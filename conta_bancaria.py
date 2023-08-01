class ContaBancaria:
    def __init__(self, numeroConta, saldo):
        self.numeroConta = numeroConta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente para o saque.")

    def detalhesConta(self):
        print(f"Conta: {self.numeroConta}")
        print(f"Saldo: R$ {self.saldo:.2f}")