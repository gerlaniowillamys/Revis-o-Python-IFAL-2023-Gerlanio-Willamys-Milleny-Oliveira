#Lista de Exercício 7 - Questão 4
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Pessoa: Faça um programa que crie uma classe que modele uma pessoa:
# A. Atributos: nome, idade, peso e altura
# B. Métodos: Envelhecer, engordar, emagrecer, crescer.
#    Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        if self.peso - peso < 0:
            raise ValueError("A pessoa não pode emagrecer mais do que seu peso atual.")
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Exemplo de uso da classe Pessoa
try:
    pessoa = Pessoa("Milleny", 18, 47, 1.59)
    print("Nome:", pessoa.nome)
    print("Idade:", pessoa.idade)
    print("Peso:", pessoa.peso)
    print("Altura:", pessoa.altura)
    pessoa.envelhecer(2)
    pessoa.engordar(5)
    pessoa.emagrecer(3)
    pessoa.crescer(2)
    print("Idade após envelhecer:", pessoa.idade)
    print("Peso após engordar:", pessoa.peso)
    print("Altura após crescer:", pessoa.altura)
except ValueError as error:
    print("Erro:", str(error))
