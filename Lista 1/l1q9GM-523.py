#Lista de Exercício 1 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print("A temperatura em graus Celsius é:", celsius)