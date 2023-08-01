
from veiculo import Veiculo, Carro, Aviao

# Criando instâncias das subclasses
carro = Carro()
aviao = Aviao()

# Chamando o método mover() de cada instância
print("Carro:")
carro.mover()

print("\nAvião:")
aviao.mover()