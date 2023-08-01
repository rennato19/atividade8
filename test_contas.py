from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
conta_corrente = ContaCorrente(numeroConta="123", saldo=1000.0, limite=500.0)
conta_poupanca = ContaPoupanca(numeroConta="456", saldo=2000.0, taxaRendimento=0.03)

# Utilizando os métodos depositar e sacar
conta_corrente.depositar(300.0)
conta_corrente.sacar(800.0)

conta_poupanca.depositar(500.0)
conta_poupanca.sacar(100.0)

# Chamando o método detalhesConta de cada classe
print("\nDetalhes da Conta Corrente:")
conta_corrente.detalhesConta()

print("\nDetalhes da Conta Poupança:")
conta_poupanca.detalhesConta()
