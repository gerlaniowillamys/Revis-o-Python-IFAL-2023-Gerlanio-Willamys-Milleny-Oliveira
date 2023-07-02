#Lista de Exercício 1 - Questão 14
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso total de peixes pescados (em quilos): "))
limite = 50.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
    print("Peso excedido:", excesso, "kg")
    print("Valor da multa a ser pago: R$", multa)
else:
    excesso = 0.0
    multa = 0.0
    print("Peso dentro do limite. Não há multa a ser paga.")