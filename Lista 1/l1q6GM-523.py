#Lista de Exercício 1 - Questão 6 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

def calcular_area_circulo(raio):
    return math.pi * raio**2

if __name__ == "__main__":
    try:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print("A área do círculo é:", area)
    except ValueError:
        print("Entrada inválida. Por favor, digite um raio válido.")
    except Exception as e:
        print("Ocorreu um erro:", e)
