#Lista de Exercício 1 - Questão 16
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

def calcular_latas_tinta(tamanho_area):
    litros_tinta = tamanho_area / 3
    latas_tinta = math.ceil(litros_tinta / 18)
    return latas_tinta

def calcular_preco_total(latas_tinta):
    return latas_tinta * 80.00

if __name__ == "__main__":
    try:
        tamanho_area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

        latas_tinta = calcular_latas_tinta(tamanho_area)
        preco_total = calcular_preco_total(latas_tinta)

        print("Quantidade de latas de tinta necessárias:", latas_tinta)
        print("Preço total das latas de tinta: R$", preco_total)
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico válido para o tamanho da área.")
    except Exception as e:
        print("Ocorreu um erro:", e)
