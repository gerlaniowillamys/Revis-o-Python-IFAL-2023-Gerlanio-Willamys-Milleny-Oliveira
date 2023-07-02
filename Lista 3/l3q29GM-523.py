#Lista de Exercício 3 - Questão 29
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para montar a tabela de preços da loja de artigos de R$ 1,99.

#O programa cria uma tabela de preços com base no número de itens que o cliente comprou.
#A tabela contém os preços de 1 até 50 produtos.

class TabelaPrecos:
    def __init__(self):
        self.tabela = {}

    def montar_tabela(self):
        for quantidade in range(1, 51):
            preco = quantidade * 1.99  # Calcula o preço com base na quantidade de itens
            self.tabela[quantidade] = preco  # Adiciona o preço na tabela

    def exibir_tabela(self):
        print("Lojas Quase Dois - Tabela de Preços:")
        for quantidade, preco in self.tabela.items():
            print(f"{quantidade} - R$ {preco:.2f}")

if __name__ == "__main__":
    tabela_precos = TabelaPrecos()
    tabela_precos.montar_tabela()  # Monta a tabela de preços
    tabela_precos.exibir_tabela()  # Exibe a tabela de preços
