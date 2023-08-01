
import math
from forma import Forma
class Circulo(Forma):
    def __init__(self, tipo, descricao, raio):
        super().__init__(tipo, descricao)
        self.raio = raio

    @property
    def calcular_area(self):
        return math.pi * self.raio ** 2

    @property
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
