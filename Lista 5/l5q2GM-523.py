#Lista de Exercício 5 - Questão 2
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

class SequenciaTriangular:
    def __init__(self, n):
        self.n = n

    def imprimir_sequencia(self):
        try:
            if self.n <= 0:
                raise ValueError("O valor de n deve ser um número inteiro positivo.")

            for i in range(1, self.n + 1):
                linha = ""
                for j in range(1, i + 1):
                    linha += str(j) + " "
                print(linha)
        except ValueError as e:
            print("Erro:", e)

    @staticmethod
    def ler_valor():
        while True:
            try:
                valor = int(input("Insira um número inteiro: "))
                sequencia = SequenciaTriangular(valor)
                sequencia.imprimir_sequencia()
                break
            except ValueError:
                print("Erro: Entrada inválida. Digite um número inteiro válido.")


SequenciaTriangular.ler_valor()
