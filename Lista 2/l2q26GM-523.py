#Lista de Exercício 2 - Questão 26
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def calcular_preco_abastecimento(litros, combustivel):
    if litros <= 0:
        raise ValueError("A quantidade de litros deve ser maior que zero.")

    if combustivel.lower() not in ["a", "g"]:
        raise ValueError("Opção de combustível inválida. Digite 'A' para álcool ou 'G' para gasolina.")

    if combustivel.lower() == "a":
        preco = litros * 1.9
        if litros <= 20:
            preco -= 1.9 * litros * 3 / 100
        else:
            preco -= 1.9 * litros * 5 / 100
    elif combustivel.lower() == "g":
        preco = litros * 2.5
        if litros <= 20:
            preco -= 2.5 * litros * 4 / 100
        else:
            preco -= 2.5 * litros * 6 / 100
    
    return preco


def main():
    try:
        litros = float(input("Digite quantos litros você quer abastecer: "))
        combustivel = input("Digite A para álcool ou G para gasolina: ")

        preco = calcular_preco_abastecimento(litros, combustivel)
        print("O preço a pagar é R${:.2f}".format(preco))
    except ValueError as error:
        print("Erro:", error)


if __name__ == "__main__":
    main()
