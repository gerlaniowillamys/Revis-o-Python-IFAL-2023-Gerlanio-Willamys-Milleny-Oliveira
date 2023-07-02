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

tamanho_area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

litros_tinta = tamanho_area / 6
latas_tinta = math.ceil(litros_tinta / 18)
galoes_tinta = math.ceil(litros_tinta / 3.6)
preco_latas = latas_tinta * 80.00
preco_galoes = galoes_tinta * 25.00

# Opção de compra apenas com latas de 18 litros
print("Opção 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas de tinta necessárias:", latas_tinta)
print("Preço total das latas de tinta: R$", preco_latas)

# Opção de compra apenas com galões de 3,6 litros
print("\nOpção 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões de tinta necessários:", galoes_tinta)
print("Preço total dos galões de tinta: R$", preco_galoes)

# Opção de misturar latas e galões
latas_mistura = int(litros_tinta / 18)
litros_restantes = litros_tinta % 18
galoes_mistura = math.ceil(litros_restantes / 3.6)
preco_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)

print("\nOpção 3: Misturar latas e galões")
print("Quantidade de latas de tinta necessárias:", latas_mistura)
print("Quantidade de galões de tinta necessários:", galoes_mistura)
print("Preço total da mistura de latas e galões: R$", preco_mistura)