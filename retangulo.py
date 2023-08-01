
from forma import Forma
class Retangulo(Forma):
    def __init__(self, tipo, descricao, lado1, lado2):
        super().__init__(tipo, descricao)
        self.lado1 = lado1
        self.lado2 = lado2

    @property
    def calcular_area(self):
        return self.lado1 * self.lado2

    @property
    def calcular_perimetro(self):
        return 2 * (self.lado1 + self.lado2)
