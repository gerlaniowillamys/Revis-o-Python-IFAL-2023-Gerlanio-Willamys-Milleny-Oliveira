#Lista de Exercício 3 - Questão 30
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para montar a tabela de preços de pães para a panificadora.

#O programa solicita ao usuário o preço do pão e cria uma tabela de preços de 1 até 50 pães.


class TabelaPrecosPaes:
    def __init__(self):
        self.preco_pao = 0
        self.tabela = {}

    def solicitar_preco_pao(self):
        while True:
            try:
                self.preco_pao = float(input("Preço do pão: R$ "))  # Solicita o preço do pão
                if self.preco_pao <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Preço inválido. Digite um valor válido.")

    def montar_tabela(self):
        for quantidade in range(1, 51):
            preco = quantidade * self.preco_pao  # Calcula o preço com base na quantidade de pães
            self.tabela[quantidade] = preco  # Adiciona o preço na tabela

    def exibir_tabela(self):
        print("Panificadora Pão de Ontem - Tabela de Preços")
        for quantidade, preco in self.tabela.items():
            print(f"{quantidade} - R$ {preco:.2f}")

if __name__ == "__main__":
    tabela_precos_paes = TabelaPrecosPaes()
    tabela_precos_paes.solicitar_preco_pao()  # Solicita o preço do pão
    tabela_precos_paes.montar_tabela()  # Monta a tabela de preços de pães
    tabela_precos_paes.exibir_tabela()  # Exibe a tabela de preços de pães
