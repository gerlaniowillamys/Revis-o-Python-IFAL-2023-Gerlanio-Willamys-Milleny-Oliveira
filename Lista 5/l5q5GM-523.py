#Lista de Exercício 5 - Questão 5
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

class CalculadoraImposto:
    def __init__(self, taxa_imposto):
        self.taxa_imposto = taxa_imposto

    def calcular_preco_com_imposto(self, custo):
        if custo < 0:
            raise ValueError("O custo do item deve ser um valor não negativo.")
        custo_total = custo * (1 + (self.taxa_imposto / 100))
        return custo_total

    @classmethod
    def ler_e_calcular(cls):
        try:
            taxa = float(input("Insira a taxa de imposto sobre vendas (%): "))
            preco = float(input("Insira o custo do item (em reais): "))
            calculadora = cls(taxa)
            preco_com_imposto = calculadora.calcular_preco_com_imposto(preco)
            print(f"O custo do item com o imposto sobre vendas é R${preco_com_imposto:.2f}")
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números.")

CalculadoraImposto.ler_e_calcular()
