#Lista de Exercício 1 - Questão 17
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

def calcular_latas_galoes(tamanho_area):
    litros_tinta = tamanho_area / 6
    latas_tinta = math.ceil(litros_tinta / 18)
    galoes_tinta = math.ceil(litros_tinta / 3.6)
    return latas_tinta, galoes_tinta

def calcular_preco_total(latas_tinta, galoes_tinta):
    preco_latas = latas_tinta * 80.00
    preco_galoes = galoes_tinta * 25.00
    return preco_latas, preco_galoes

def calcular_mistura(litros_tinta):
    latas_mistura = int(litros_tinta / 18)
    litros_restantes = litros_tinta % 18
    galoes_mistura = math.ceil(litros_restantes / 3.6)
    preco_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)
    return latas_mistura, galoes_mistura, preco_mistura

if __name__ == "__main__":
    try:
        tamanho_area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

        latas_tinta, galoes_tinta = calcular_latas_galoes(tamanho_area)
        preco_latas, preco_galoes = calcular_preco_total(latas_tinta, galoes_tinta)
        latas_mistura, galoes_mistura, preco_mistura = calcular_mistura(tamanho_area / 6)

        # Opção de compra apenas com latas de 18 litros
        print("Opção 1: Comprar apenas latas de 18 litros")
        print("Quantidade de latas de tinta necessárias:", latas_tinta)
        print("Preço total das latas de tinta: R$", preco_latas)

        # Opção de compra apenas com galões de 3,6 litros
        print("\nOpção 2: Comprar apenas galões de 3,6 litros")
        print("Quantidade de galões de tinta necessários:", galoes_tinta)
        print("Preço total dos galões de tinta: R$", preco_galoes)

        # Opção de misturar latas e galões
        print("\nOpção 3: Misturar latas e galões")
        print("Quantidade de latas de tinta necessárias:", latas_mistura)
        print("Quantidade de galões de tinta necessários:", galoes_mistura)
        print("Preço total da mistura de latas e galões: R$", preco_mistura)

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico válido para o tamanho da área.")
    except Exception as e:
        print("Ocorreu um erro:", e)
