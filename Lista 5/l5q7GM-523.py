#Lista de Exercício 5 - Questão 7
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor, dias_atraso):
    if dias_atraso <= 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * (0.001 * dias_atraso)
        return valor + multa + juros

relatorio = {
    'quantidade': 0,
    'valor_total': 0,
}

while True:
    valor_prestacao = float(input("Insira o valor da prestação (ou 0 para encerrar): "))
    if valor_prestacao == 0:
        break

    dias_atraso = int(input("Insira o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)

    print(f"O valor a ser pago é R${valor_a_pagar:.2f}")

    relatorio['quantidade'] += 1
    relatorio['valor_total'] += valor_a_pagar

print(f"Relatório do dia:\\nQuantidade de prestações pagas: {relatorio['quantidade']}\\nValor total das prestações pagas: R${relatorio['valor_total']:.2f}")