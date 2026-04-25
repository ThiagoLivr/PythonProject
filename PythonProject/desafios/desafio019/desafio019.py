import time

from rich import print
from time import sleep

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Voce acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.total_paginas}[/] páginas no total. Voce agora está na [yellow]página {self.pagina_atual}[/]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                time.sleep(0.2)
                cont += 1
        print(f"[blue]Voce avançou {cont} páginas e agora esta na [yellow]página {self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Voce chegou ao final do livro {self.titulo}[/]")


    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False


l1 = Livro(titulo = "10 coisas que aprendi", paginas = 20)
print(l1.avancar_paginas(10))
