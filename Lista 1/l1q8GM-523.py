#Lista de Exercício 1 - Questão 8 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def calcular_salario_total(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas

if __name__ == "__main__":
    try:
        valor_hora = float(input("Digite o valor do salário por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        salario_total = calcular_salario_total(valor_hora, horas_trabalhadas)
        print("O total do seu salário no mês é:", salario_total)
    except ValueError:
        print("Entrada inválida. Por favor, digite valores válidos para o valor do salário por hora e para o número de horas trabalhadas.")
    except Exception as e:
        print("Ocorreu um erro:", e)
