
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


class Animal():
    def __init__(self,nome,cor,sexo):
        self.nome=nome
        self.cor=cor
        self.sexo=sexo

    def comer(self):
        print(f"O {self.nome} foi comer...")


class Gato(Animal):
    def __init__(self,nome,cor,sexo):
        super().__init__(nome,cor,sexo)

    def miar(self):
        print(f"O {self.nome} foi miando...")


class Vaca(Animal):
    def __init__(self,nome,cor,sexo):
        super().__init__(nome,cor,sexo)

    def mugir(self):
        print(f"O {self.nome} foi mugindo...")


class Coelho(Animal):
    def __init__(self,nome,cor,sexo):
        super().__init__(nome,cor,sexo)

    def pular(self):
        print(f"O {self.nome} foi pulando...")


class Cachorro(Animal):
    def __init__(self, nome, cor,sexo):
                super().__init__(nome,cor,sexo)

    def latir(self):
                print(f"O {self.nome} foi latindo...")

#---------------------------

class Ingresso():
    def __init__(self,valor):
        self.valor= valor

    def imprimevalor(self,valor):
        print(f"O valor do ingresso será {valor}")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)

    def ingressovip2(self):
        adicional = self.valor * 1.5


        print(f"O valor adicional foi {adicional}")

