#Lista de Exercício 3 - Questão 41
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
def calcular_parcelas_divida(divida):
    tabela_juros = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }

    print("Valor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")
    for parcelas, juros in tabela_juros.items():
        valor_juros = (divida * juros) / 100
        valor_total = divida + valor_juros
        valor_parcela = valor_total / parcelas
        print(f"R$ {divida:.2f}\t\tR$ {valor_juros:.2f}\t\t{parcelas}\t\t\tR$ {valor_parcela:.2f}")


# Exemplo de uso
valor_divida = float(input("Digite o valor da dívida: "))
calcular_parcelas_divida(valor_divida)