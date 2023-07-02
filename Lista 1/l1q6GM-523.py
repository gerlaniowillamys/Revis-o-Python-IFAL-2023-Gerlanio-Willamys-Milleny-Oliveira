#Lista de Exercício 1 - Questão 6 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio**2

print("A área do círculo é:", area)