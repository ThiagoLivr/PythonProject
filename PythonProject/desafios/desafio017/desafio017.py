from rich import print
from rich.panel import Panel
from rich.text import Text

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Panel(Text(f"{self.nome}\n{"":-^30}\nR$:{self.preco:,.2f}", justify = "center"), title = "Produto", width = 34)

p1 = Produto("iPhone 17 Pro Max", 25_000.00)
print(p1.etiqueta())

p2 = Produto("Notebook Gamer", 8_000)
print(p2.etiqueta())