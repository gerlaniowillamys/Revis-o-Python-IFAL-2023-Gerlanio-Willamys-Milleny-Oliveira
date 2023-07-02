#Lista de Exercício 2 - Questão 8
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o valor do primeiro produto: "))
prod2 = float(input("Digite o valor do segundo produto: "))
prod3 = float(input("Digite o valor do terceiro produto: "))

if (prod1 < prod2 and prod1 < prod3):
    print("O primeiro produto é o mais barato.")

elif (prod2 < prod1 and prod2 < prod3):
    print("O segundo produto é o mais barato.")

elif (prod3 < prod1 and prod3 < prod2):
    print("O terceiro produto é o mais barato.")