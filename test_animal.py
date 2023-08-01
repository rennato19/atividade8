
from animal import Animal, Cachorro, Gato

# Criando instâncias das subclasses
animal_generico = Animal()
cachorro = Cachorro()
gato = Gato()

# Chamando o método emitir_som() de cada instância
print("Animal genérico:")
animal_generico.emitir_som()

print("\nCachorro:")
cachorro.emitir_som()

print("\nGato:")
gato.emitir_som()