#Lista de Exercício 2 - Questão 28
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne(tipo, quantidade, usar_cartao):
    if tipo < 1 or tipo > 3 or quantidade <= 0:
        raise ValueError("Valores inválidos para tipo ou quantidade.")

    if tipo == 1:
        nome = "File Duplo"
        if quantidade <= 5:
            preco = quantidade * 4.90
        else:
            preco = quantidade * 5.80
    elif tipo == 2:
        nome = "Alcatra"
        if quantidade <= 5:
            preco = quantidade * 5.90
        else:
            preco = quantidade * 6.80
    elif tipo == 3:
        nome = "Picanha"
        if quantidade <= 5:
            preco = quantidade * 6.90
        else:
            preco = quantidade * 7.80

    if usar_cartao:
        r = "SIM"
        desconto = preco * 0.05
        total = preco - desconto
    else:
        r = "NAO"
        total = preco

    return nome, quantidade, preco, r, total


def main():
    try:
        print("1- File Duplo\n2- Alcatra\n3- Picanha")
        tipo = int(input("Digite o tipo: "))
        quantidade = int(input("Digite a quantidade comprada: "))
        resposta = int(input("A compra será realizada com cartão Tabajara? 1 para SIM - 2 para NAO: "))

        nome, qtd, preco, cartao, total = calcular_preco_carne(tipo, quantidade, resposta == 1)

        print("\n***************************CUPOM FISCAL**************************************")
        print("* Carne..........................................................", nome)
        print("* Quantidade.....................................................", qtd, "KG")
        print("* Preço.........................................................", "%.2f" % preco, "R$")
        print("* Cartão Tabajara................................................", cartao)
        print("* Total com desconto............................................", "%.2f" % total, "R$")
        print("******************************************************************************")
    except ValueError as error:
        print("Erro:", error)


if __name__ == "__main__":
    main()
