#Lista de Exercício 2 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def obter_dia_semana(numero):
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    try:
        dia_semana = dias_semana[numero]
        print("O referente ao número foi: {}".format(dia_semana))
    except KeyError:
        print("Número não referente a um dia da semana")

dia = int(input("Escolha um número referente ao dia da semana: "))
obter_dia_semana(dia)
