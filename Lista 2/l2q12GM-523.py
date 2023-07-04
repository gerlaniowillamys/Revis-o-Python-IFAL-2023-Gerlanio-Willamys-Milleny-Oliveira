#Lista de Exercício 2 - Questão 12
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

def calcular_salario_liquido(salario_bruto):
    try:
        sind = (3 * salario_bruto) / 100
        fgts = (11 * salario_bruto) / 100

        salario_liquido = salario_bruto - sind

        print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
        print("Desconto do Sindicato: R$ {:.2f}".format(sind))
        print("Salário Líquido: R$ {:.2f}".format(salario_liquido))
        print("Valor do FGTS: R$ {:.2f}".format(fgts))
    except ValueError:
        print("Erro: Valor inválido.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")

salario = float(input("Digite seu salário bruto: "))
calcular_salario_liquido(salario)
