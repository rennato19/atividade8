class Forma:
    def __init__(self, tipo, descricao):
        self.tipo = tipo
        self.descricao = descricao

    def dadosDaForma(self):
        return f"Tipo: {self.tipo}, Descrição: {self.descricao}"

    @property
    def calcular_area(self):
        return "Não há dados suficientes para realizar o cálculo."

    @property
    def calcular_perimetro(self):
        return "Não há dados suficientes para realizar o cálculo."
