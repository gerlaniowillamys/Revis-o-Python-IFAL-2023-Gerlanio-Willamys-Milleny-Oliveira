#Lista de Exercício 2 - Questão 16
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
    
import math


class EquacaoQuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_raizes(self):
        if self.a == 0:
            raise ValueError("A equação não é do segundo grau.")

        delta = self.b ** 2 - 4 * self.a * self.c

        if delta < 0:
            raise ValueError("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -self.b / (2 * self.a)
            return [raiz]
        else:
            raiz1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return [raiz1, raiz2]


def main():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        equacao = EquacaoQuadratica(a, b, c)
        raizes = equacao.calcular_raizes()
        print("As raízes da equação são:", raizes)
    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()
