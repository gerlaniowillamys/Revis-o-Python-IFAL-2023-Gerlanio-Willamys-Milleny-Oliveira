#Lista de Exercício 4 - Questão 5
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler 20 números inteiros, separar os números pares e ímpares em vetores diferentes e imprimir os três vetores.

class SeparadorNumeros:
    def __init__(self):
        self.vetor = []  # Lista vazia para armazenar os números inteiros
        self.pares = []  # Lista vazia para armazenar os números pares
        self.impares = []  # Lista vazia para armazenar os números ímpares

    def ler_numeros(self):
        # Função para ler os números inteiros e armazená-los no vetor
        try:
            for i in range(20):
                numero = int(input(f"Digite o número {i+1}: "))
                self.vetor.append(numero)
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

    def separar_numeros(self):
        # Função para separar os números pares e ímpares em vetores diferentes
        for numero in self.vetor:
            if numero % 2 == 0:
                self.pares.append(numero)
            else:
                self.impares.append(numero)

    def imprimir_vetores(self):
        # Função para imprimir os três vetores
        print("Vetor completo:", self.vetor)
        print("Números pares:", self.pares)
        print("Números ímpares:", self.impares)

# Cria um objeto da classe SeparadorNumeros
separador = SeparadorNumeros()

# Chama a função ler_numeros para ler os números inteiros
separador.ler_numeros()

# Chama a função separar_numeros para separar os números pares e ímpares
separador.separar_numeros()

# Chama a função imprimir_vetores para imprimir os três vetores
separador.imprimir_vetores()
