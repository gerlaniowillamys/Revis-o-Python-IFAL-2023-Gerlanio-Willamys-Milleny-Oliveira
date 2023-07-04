#Lista de Exercício 3 - Questão 28
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Programa para calcular o valor total investido em uma coleção de CDs e o valor médio gasto em cada um.

#O programa solicita a quantidade de CDs e o valor de cada um.
#Em seguida, calcula o valor total investido na coleção e o valor médio gasto em cada CD.


class ValorInvalidoError(Exception):
    pass

class ColecaoCDs:
    def __init__(self):
        self.num_cds = 0
        self.total_investido = 0

    def solicitar_quantidade_cds(self):
        while True:
            try:
                self.num_cds = int(input("Digite a quantidade de CDs na coleção: "))  # Solicita a quantidade de CDs
                if self.num_cds <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro maior que zero.")

    def solicitar_valor_cds(self):
        for i in range(self.num_cds):
            while True:
                try:
                    valor = float(input(f"Digite o valor do CD {i + 1}: R$"))  # Solicita o valor do CD
                    if valor <= 0:
                        raise ValorInvalidoError
                    self.total_investido += valor  
                    # Adiciona o valor do CD ao total investido
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")
                except ValorInvalidoError:
                    print("Valor inválido. Digite um valor maior que zero.")

    def calcular_valor_medio(self):
        if self.num_cds == 0:
            return 0
        return self.total_investido / self.num_cds  
        # Calcula o valor médio gasto em cada CD

    def exibir_resultado(self):
        print(f"Valor total investido na coleção: R${self.total_investido:.2f}")
        valor_medio = self.calcular_valor_medio()
        print(f"Valor médio gasto em cada CD: R${valor_medio:.2f}")

if __name__ == "__main__":
    colecao = ColecaoCDs()
    colecao.solicitar_quantidade_cds()  # Solicita a quantidade de CDs na coleção
    colecao.solicitar_valor_cds()  # Solicita o valor de cada CD
    colecao.exibir_resultado()  # Exibe o resultado do valor total investido e do valor médio gasto em cada CD
