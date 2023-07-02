#Lista de Exercício 1 - Questão 12
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite a altura da pessoa em metros: "))

peso_ideal = (72.7 * altura) - 58

print("O peso ideal para essa altura é:", peso_ideal, "kg")