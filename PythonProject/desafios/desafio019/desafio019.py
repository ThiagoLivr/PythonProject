from rich import print

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: Voce acabou de abrir o livro {self.titulo} que tem {self.total_paginas} paginas no total. Voce agora esta na pagina {self.pagina_atual}")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            self.pagina_atual += 1
            print(f"Agora voce esta na pagina {self.pagina_atual}")
            cont += 1

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return False
        else:
            return True


l1 = Livro(titulo = "10 coisas que aprendi", paginas = 20)
print(l1.avancar_paginas(5))
