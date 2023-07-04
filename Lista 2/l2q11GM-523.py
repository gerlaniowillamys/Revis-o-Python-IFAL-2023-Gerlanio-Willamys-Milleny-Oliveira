#Lista de Exercício 2 - Questão 11
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

def calcular_aumento_salario(salario):
    if salario <= 280:
        percentual = 20
    elif salario < 700:
        percentual = 15
    elif salario < 1500:
        percentual = 10
    else:
        percentual = 5

    aumento = (percentual * salario) / 100
    salario_final = salario + aumento

    return percentual, aumento, salario_final


def main():
    try:
        salario = float(input("Digite seu salário (R$): "))
        percentual, aumento, salario_final = calcular_aumento_salario(salario)

        print("Seu salário é de: R${}".format(salario))
        print("Percentual de aumento: {}%".format(percentual))
        print("O aumento foi de: R${}".format(aumento))
        print("O Salário final é de: R${}".format(salario_final))
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um número válido para o salário.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")


if __name__ == "__main__":
    main()
