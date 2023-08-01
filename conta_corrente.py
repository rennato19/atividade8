from conta_bancaria import ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, numeroConta, saldo, limite):
        super().__init__(numeroConta, saldo)
        self.limite = limite

    def detalhesConta(self):
        super().detalhesConta()
        print(f"Limite do Cheque Especial: R$ {self.limite:.2f}")