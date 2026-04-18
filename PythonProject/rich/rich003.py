from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Precos")

tabela.add_column("Nome")
tabela.add_column("Preco")

tabela.add_row("Lapis", "R$1,50")
tabela.add_row("Borracha", "R$5,00")

print(tabela)