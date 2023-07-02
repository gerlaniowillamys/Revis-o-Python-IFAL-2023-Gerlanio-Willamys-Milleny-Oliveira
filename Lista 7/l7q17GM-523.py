#Lista de Exercício 7 - Questão 17
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#fazenda de bichinhos

import random

class Bichinho: #classe Bichinho, que representa um bichinho individual com atributos como nome, nível de fome e tédio.
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

    def comer(self):
        self.fome -= 1
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.tedio -= 1
        if self.tedio < 0:
            self.tedio = 0

    def falar(self):
        print(f"{self.nome}: Estou com fome = {self.fome}, estou entediado = {self.tedio}")


class Fazenda: #classe Fazenda mantém uma lista de bichinhos e fornece métodos para realizar ações em todos os bichinhos ao mesmo tempo.
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_bichinhos(self):
        for bichinho in self.bichinhos:
            bichinho.comer()

    def brincar_com_bichinhos(self):
        for bichinho in self.bichinhos:
            bichinho.brincar()

    def ouvir_bichinhos(self):
        for bichinho in self.bichinhos:
            bichinho.falar()


def exibir_menu(): #o programa exibe um menu para o usuário escolher as opções disponíveis
    print("\n===== Fazenda de Bichinhos =====")
    print("1. Adicionar Bichinho")
    print("2. Alimentar Bichinhos")
    print("3. Brincar com Bichinhos")
    print("4. Ouvir Bichinhos")
    print("5. Sair")


fazenda = Fazenda()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do bichinho: ")
        bichinho = Bichinho(nome)
        fazenda.adicionar_bichinho(bichinho)
        print(f"{nome} foi adicionado(a) à fazenda!")

    elif opcao == "2":
        fazenda.alimentar_bichinhos()
        print("Todos os bichinhos foram alimentados!")

    elif opcao == "3":
        fazenda.brincar_com_bichinhos()
        print("Todos os bichinhos brincaram!")

    elif opcao == "4":
        fazenda.ouvir_bichinhos()

    elif opcao == "5":
        print("Obrigado por jogar!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
