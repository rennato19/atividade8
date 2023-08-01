
from conta_bancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta, saldo, taxaRendimento):
        super().__init__(numeroConta, saldo)
        self.taxaRendimento = taxaRendimento

    def detalhesConta(self):
        super().detalhesConta()
        print(f"Taxa de Rendimento: {self.taxaRendimento * 100:.2f}%")