from biblioteca import *

aluno01 = Pessoa("Julia do CAC", 18, 55)
aluno02 = Pessoa("Vitinho Seaway", 52, 18)



print(aluno01.nome)
print(aluno02.nome)

aluno01.apresentar()
aluno01.comer()

aluno02.apresentar()

aluno01.comer()


aninha = Gato("Rosa","parda","feminino")
aninha.miar()

lala= Vaca("Analice","branca","feminino")
lala.mugir()

branco= Cachorro("branco","preto","masculino")
branco.latir()

doutora= Coelho("doutora","branco","feminino")
doutora.pular()


valor= Ingresso(250)
valores1= Vip(50)
valores1.ingressovip2()