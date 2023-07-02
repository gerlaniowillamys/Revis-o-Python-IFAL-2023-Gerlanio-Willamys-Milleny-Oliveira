#Lista de Exercício 4 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para calcular a soma dos quadrados dos elementos de um vetor.

class CalculadoraQuadrados:
    def __init__(self):
        self.vetor = []  # Lista vazia para armazenar os números inteiros

    def ler_vetor(self):
        # Função para ler os números inteiros e armazená-los no vetor
        try:
            for i in range(10):
                numero = int(input(f"Digite o número {i+1}: "))
                self.vetor.append(numero)
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

    def calcular_soma_quadrados(self):
        # Função para calcular a soma dos quadrados dos elementos do vetor
        soma = 0
        for numero in self.vetor:
            quadrado = numero ** 2
            soma += quadrado
        return soma

# Cria um objeto da classe CalculadoraQuadrados
calculadora = CalculadoraQuadrados()

# Chama a função ler_vetor para ler os números inteiros
calculadora.ler_vetor()

# Chama a função calcular_soma_quadrados para calcular a soma dos quadrados dos elementos do vetor
soma_quadrados = calculadora.calcular_soma_quadrados()

# Imprime a soma dos quadrados dos elementos do vetor
print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)
