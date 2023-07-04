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
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def envelhecer(self, anos):
        self._idade += anos
        if self._idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        if peso < 0:
            raise ValueError("A quantidade de peso a ser adicionado deve ser um valor positivo.")
        self._peso += peso

    def emagrecer(self, peso):
        if peso < 0 or self._peso - peso < 0:
            raise ValueError("A quantidade de peso a ser removido é inválida.")
        self._peso -= peso

    def crescer(self, altura):
        if altura < 0:
            raise ValueError("A quantidade de altura a ser adicionada deve ser um valor positivo.")
        self._altura += altura

    def mostrarInformacoes(self):
        return "Nome: {}, Idade: {}, Peso: {}, Altura: {}".format(self._nome, self._idade, self._peso, self._altura)

# Exemplo de uso da classe Pessoa
try:
    pessoa = Pessoa("Milleny", 18, 47, 1.59)
    print(pessoa.mostrarInformacoes())
    pessoa.envelhecer(2)
    pessoa.engordar(5)
    pessoa.emagrecer(3)
    pessoa.crescer(2)
    print(pessoa.mostrarInformacoes())
except ValueError as error:
    print("Erro:", str(error))
