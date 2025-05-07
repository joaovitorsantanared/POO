from operator import truediv


class Pessoa():
    def __init__(self,nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade

    def apresentar(self):
        print(f"Meu nome é {self.nome}")
        print(f"Eu tenho {self.idade} anos e pes {self.peso}")

    def comer(self):
        print(f"{self.nome} está comendo")

    def dormir(self):
        print(f"{self.nome} está dormindo")


    def falar(self):
        print(f"{self.nome} está falar")





