#Lista de Exercício 2 - Questão 14
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = ((nota1+nota2)/2)

if (media < 4):
    print("E, REPROVADO!")

elif (media >= 4 and media < 6):
    print("D, REPROVADO!")

elif (media >= 6 and media < 7.5):
    print("C, APROVADO!")

elif (media >= 7.5 and media < 9):
    print("B, APROVADO!")

elif  (media >= 9):
    print("A, APROVADO!")