#Lista de Exercício 5 - Questão 1 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir_sequencia_triangular(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("O valor de n deve ser um número inteiro positivo.")
        
        for i in range(1, n+1):
            linha = ''
            for j in range(i):
                linha += str(i)
            print(linha)
    except ValueError as e:
        print("Erro:", e)


def ler_valor():
    while True:
        try:
            valor = input('Digite um valor para n: ')
            imprimir_sequencia_triangular(valor)
            break
        except ValueError as e:
            print("Erro:", e)


ler_valor()
