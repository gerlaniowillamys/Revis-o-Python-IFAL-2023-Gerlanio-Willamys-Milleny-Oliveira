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

def imprimir_sequencia(n):
    for i in range(1, n+1):
        linha = ""
        for j in range(1, i+1):
            linha += str(j) + " "
        print(linha)

n = int(input("Insira um número inteiro: "))
imprimir_sequencia(n)