#Lista de Exercício 2 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("Escolha um número referente ao dia da semana: "))

if (dia == 1):
    print("O referente ao número foi: Domingo,")

elif (dia == 2):
    print("O referente ao número foi: Segunda-feira.")

elif (dia == 3):
    print("O referente ao número foi: Terça-feira.")

elif (dia == 4):
    print("O referente ao número foi: Quarta-feira.")

elif (dia == 5):
    print("O referente ao número foi: Quinta-feira.")

elif (dia == 6):
    print("O referente ao número foi: Sexta-feira.")

elif (dia == 7):
    print("O referente ao número foi: Sábado.")

else:
    print("Número não referente.")