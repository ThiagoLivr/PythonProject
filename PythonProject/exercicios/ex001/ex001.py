#Declaracao de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atibutos de Instancia
        self.nome = ""
        self.idade = 0

    # Metodos da Instancia
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaracao de Objeto
g1 = Gafanhoto()
g1.nome = "Millene"
g1.idade = 28
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Thiago"
g2.idade = 28
g2.aniversario()
print(g2.mensagem())