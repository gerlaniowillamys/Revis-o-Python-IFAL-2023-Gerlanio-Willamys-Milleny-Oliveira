#Lista de Exercício 7 - Questão 8
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estômago)
# e pelo menos os métodos comer(), verBucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com
# pelo menos 3 alimentos diferentes e verificando o conteúdo do estômago a cada refeição.
# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if self.bucho:
            print(f"Conteúdo do estômago de {self.nome}:")
            for alimento in self.bucho:
                print(alimento)
        else:
            print(f"O estômago de {self.nome} está vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"O estômago de {self.nome} já está vazio.")

# Exemplo de uso da classe Macaco
macaco1 = Macaco("tik")
macaco2 = Macaco("tek")

macaco1.comer("Banana")
macaco1.comer("Macarrão")
macaco1.comer("Chocolate")

macaco2.comer("Laranja")
macaco2.comer("bolo")
macaco2.comer("lasanha")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()
