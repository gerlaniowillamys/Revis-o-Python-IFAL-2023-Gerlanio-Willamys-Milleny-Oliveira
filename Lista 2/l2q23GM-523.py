#Lista de Exercício 2 - Questão 23
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Digite um número: "))

if (num % 1 == 0):
    print("Inteiro")
    
else:
    print("Decimal")