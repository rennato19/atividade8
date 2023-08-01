
from forma import Forma
from circulo import Circulo
from retangulo import Retangulo
# Criando instâncias das subclasses
circulo = Circulo("Círculo", "Círculo de raio 5", 5)
retangulo = Retangulo("Retângulo", "Retângulo de lados 4 e 6", 4, 6)

# Testando as propriedades das formas
print("Dados da forma:")
print(circulo.dadosDaForma())
print(retangulo.dadosDaForma())

# Testando o cálculo da área e do perímetro
print("\nCírculo:")
print("Área:", circulo.calcular_area)
print("Perímetro:", circulo.calcular_perimetro)

print("\nRetângulo:")
print("Área:", retangulo.calcular_area)
print("Perímetro:", retangulo.calcular_perimetro)
