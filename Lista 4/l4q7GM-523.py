#Lista de Exercício 4 - Questão 7
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler um vetor de 5 números inteiros, calcular a soma, a multiplicação e imprimir os números.

class OperacoesVetor:
    def __init__(self):
        self.vetor = []  # Lista vazia para armazenar os números inteiros

    def ler_vetor(self):
        # Função para ler os números inteiros e armazená-los no vetor
        try:
            for i in range(5):
                numero = int(input(f"Digite o número {i+1}: "))
                self.vetor.append(numero)
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

    def calcular_soma(self):
        # Função para calcular a soma dos números do vetor
        soma = sum(self.vetor)
        return soma

    def calcular_multiplicacao(self):
        # Função para calcular a multiplicação dos números do vetor
        multiplicacao = 1
        for numero in self.vetor:
            multiplicacao *= numero
        return multiplicacao

    def imprimir_resultados(self):
        # Função para imprimir a soma, a multiplicação e os números do vetor
        print("Números do vetor:", self.vetor)
        print("Soma dos números:", self.calcular_soma())
        print("Multiplicação dos números:", self.calcular_multiplicacao())

# Cria um objeto da classe OperacoesVetor
operacoes = OperacoesVetor()

# Chama a função ler_vetor para ler os números inteiros
operacoes.ler_vetor()

# Chama a função imprimir_resultados para imprimir a soma, a multiplicação e os números do vetor
operacoes.imprimir_resultados()
