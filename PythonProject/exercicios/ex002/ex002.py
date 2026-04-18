#Declaracao de Classe
class Gafanhoto:
    def __init__(self, n = "", i = 0): # Método Construtor
        # Atibutos de Instancia
        self.nome = n
        self.idade = i

    # Metodos da Instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome={self.nome}, idade={self.idade}"


# Declaracao de Objeto
g1 = Gafanhoto("Millene",28)
print(g1.__getstate__()) #Method
print(g1.__dict__) #Attribute

