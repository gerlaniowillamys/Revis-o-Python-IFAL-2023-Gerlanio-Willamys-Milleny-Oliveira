#Lista de Exercício 2 - Questão 17
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano qualquer: "))

anoB = ano % 4

if (anoB == 0):
    print("O ano é bissexto.")

else:
    print("O ano não é bissexto.")
