class Churrasco:

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = 0

    def consumo(self, valor):
        self.quant += 0.400

    def kilograma(self, valor):
        self.kilograma = 1.00

    def preco(self, kilograma):
        self.preco = 82.40 / kilograma
        return self.preco

    def total(self):
        self.total = self.quant

