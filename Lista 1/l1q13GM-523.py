#Lista de Exercício 1 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem com essa altura é:", peso_ideal, "kg")
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com essa altura é:", peso_ideal, "kg")
else:
    print("Opção de sexo inválida. Por favor, digite M para masculino ou F para feminino.")