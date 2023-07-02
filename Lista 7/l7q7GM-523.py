#Lista de Exercício 7 - Questão 7
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Bichinho Virtual: Faça um programa que crie uma classe que modele um Tamagotchi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagotchi,
#      este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
#      então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome, fome=50, saude=100, idade=2):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor da fome não pode ser negativo.")
        self.fome = novo_valor

    def alterarSaude(self, novo_valor):
        if novo_valor < 0 or novo_valor > 100:
            raise ValueError("O valor da saúde deve estar entre 0 e 100.")
        self.saude = novo_valor

    def alterarIdade(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor da idade não pode ser negativo.")
        self.idade = novo_valor

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        return self.fome + self.saude

# Exemplo de uso da classe BichinhoVirtual
try:
    tamagotchi = BichinhoVirtual("noah")
    print("Nome:", tamagotchi.retornarNome())
    print("Fome:", tamagotchi.retornarFome())
    print("Saúde:", tamagotchi.retornarSaude())
    print("Idade:", tamagotchi.retornarIdade())
    tamagotchi.alterarNome("nick")
    tamagotchi.alterarFome(70)
    tamagotchi.alterarSaude(95)
    tamagotchi.alterarIdade(2)
    print("Nome após alteração:", tamagotchi.retornarNome())
    print("Fome:", tamagotchi.retornarFome())
    print("Saúde:", tamagotchi.retornarSaude())
    print("Idade:", tamagotchi.retornarIdade())
    print("Humor:", tamagotchi.retornarHumor())
except ValueError as error:
    print("Erro:", str(error))
