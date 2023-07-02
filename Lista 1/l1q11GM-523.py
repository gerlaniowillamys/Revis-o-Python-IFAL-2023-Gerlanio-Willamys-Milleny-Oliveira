#Lista de Exercício 1 - Questão 11
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite o número real: "))

produto = (2 * num1) * (num2 / 2)
soma = (3 * num1) + num3
cubo = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é:", produto)
print("A soma do triplo do primeiro com o terceiro é:", soma)
print("O terceiro número elevado ao cubo é:", cubo)