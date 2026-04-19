class Churrasco:

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
        self.consumopadrao = 0.4
        self.kilograma = 1.0


    def consumototal(self):
        consumototal = self.quant * self.consumopadrao
        return consumototal

    def preco(self):
        preco = 82.40 * self.quant
        return preco

    def total(self):
        self.total = self.quant


c1 = Churrasco('Churrasco dos Amigos', 15)

print(c1.preco())