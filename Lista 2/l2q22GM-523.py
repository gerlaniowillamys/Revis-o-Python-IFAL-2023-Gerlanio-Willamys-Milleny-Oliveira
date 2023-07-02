#Lista de Exercício 2 - Questão 22
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input("Digite um número: "))

p_i  = num % 2

if (p_i == 1):
    print("Impar.")

elif (p_i == 0):
    print("Par.")