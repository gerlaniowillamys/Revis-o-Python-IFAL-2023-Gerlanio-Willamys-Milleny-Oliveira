#Lista de Exercício 1 - Questão 15
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido

def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas

def calcular_desconto_ir(salario_bruto):
    return salario_bruto * 0.11

def calcular_desconto_inss(salario_bruto):
    return salario_bruto * 0.08

def calcular_desconto_sindicato(salario_bruto):
    return salario_bruto * 0.05

def calcular_salario_liquido(salario_bruto, desconto_ir, desconto_inss, desconto_sindicato):
    return salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

if __name__ == "__main__":
    try:
        valor_hora = float(input("Digite o valor ganho por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

        salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas)
        desconto_ir = calcular_desconto_ir(salario_bruto)
        desconto_inss = calcular_desconto_inss(salario_bruto)
        desconto_sindicato = calcular_desconto_sindicato(salario_bruto)
        salario_liquido = calcular_salario_liquido(salario_bruto, desconto_ir, desconto_inss, desconto_sindicato)

        print("Salário Bruto: R$", salario_bruto)
        print("Desconto do Imposto de Renda (11%): R$", desconto_ir)
        print("Desconto do INSS (8%): R$", desconto_inss)
        print("Desconto do Sindicato (5%): R$", desconto_sindicato)
        print("Salário Líquido: R$", salario_liquido)
    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos válidos para o valor ganho por hora e para o número de horas trabalhadas.")
    except Exception as e:
        print("Ocorreu um erro:", e)
