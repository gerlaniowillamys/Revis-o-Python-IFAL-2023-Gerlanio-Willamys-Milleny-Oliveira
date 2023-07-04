#Lista de Exercício 2 - Questão 21
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

class SaqueNotas:
    def __init__(self, valor):
        self.valor = valor
        self.cem = 0
        self.cinquenta = 0
        self.dez = 0
        self.cinco = 0
        self.um = 0

    def calcular_notas(self):
        if self.valor < 10 or self.valor > 600:
            raise ValueError("Valor inválido. Digite um valor entre 10 e 600.")

        self.cem = int(self.valor / 100)
        self.valor -= self.cem * 100

        self.cinquenta = int(self.valor / 50)
        self.valor -= self.cinquenta * 50

        self.dez = int(self.valor / 10)
        self.valor -= self.dez * 10

        self.cinco = int(self.valor / 5)
        self.valor -= self.cinco * 5

        self.um = self.valor

    def exibir_notas(self):
        print("Notas R$100,00 = {}".format(self.cem))
        print("Notas R$ 50,00 = {}".format(self.cinquenta))
        print("Notas R$ 10,00 = {}".format(self.dez))
        print("Notas R$  5,00 = {}".format(self.cinco))
        print("Notas R$  1,00 = {}".format(self.um))


def main():
    try:
        valor = int(input('Valor para sacar [10-600]: '))
        saque = SaqueNotas(valor)
        saque.calcular_notas()
        saque.exibir_notas()
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
