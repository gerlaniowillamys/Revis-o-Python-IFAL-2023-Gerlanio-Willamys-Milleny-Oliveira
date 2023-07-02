#Lista de Exercício 3 - Questão 38
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para calcular o salário atual de um funcionário com base nas regras de aumento salarial anual.

#O funcionário foi contratado em 1995 com um salário inicial.
#A partir de 1996, ele recebe um aumento anual de acordo com as regras estabelecidas.
#O programa permite que o usuário informe o salário inicial do funcionário.


import datetime

def calcular_salario_atual(salario_inicial):
    salario_atual = salario_inicial
    percentual_aumento = 0.015  # 1.5% de aumento no primeiro ano

    for ano in range(1996, datetime.datetime.now().year + 1):
        aumento = salario_atual * percentual_aumento
        salario_atual += aumento
        percentual_aumento *= 2  # O percentual dobra a cada ano

    return salario_atual

if __name__ == "__main__":
    try:
        salario_inicial = float(input("Digite o salário inicial do funcionário: "))
        salario_atual = calcular_salario_atual(salario_inicial)
        print(f"O salário atual do funcionário é: R$ {salario_atual:.2f}")
    except ValueError:
        print("Valor inválido. Digite novamente.")

