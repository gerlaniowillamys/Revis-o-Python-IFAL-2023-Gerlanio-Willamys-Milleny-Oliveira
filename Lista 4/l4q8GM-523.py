#Lista de Exercício 4 - Questão 8
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler a idade e a altura de 5 pessoas, armazenar em vetores e imprimir na ordem inversa.

class InformacoesPessoais:
    def __init__(self):
        self.idades = []  # Lista vazia para armazenar as idades
        self.alturas = []  # Lista vazia para armazenar as alturas

    def ler_informacoes(self):
        # Função para ler a idade e a altura de cada pessoa e armazená-las nos vetores
        try:
            for i in range(5):
                idade = int(input(f"Digite a idade da pessoa {i+1}: "))
                altura = float(input(f"Digite a altura da pessoa {i+1}: "))
                self.idades.append(idade)
                self.alturas.append(altura)
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro para a idade e um número real para a altura.")

    def imprimir_informacoes_inverso(self):
        # Função para imprimir a idade e a altura na ordem inversa
        print("Idades na ordem inversa:")
        for idade in reversed(self.idades):
            print(idade)

        print("\nAlturas na ordem inversa:")
        for altura in reversed(self.alturas):
            print(altura)

# Cria um objeto da classe InformacoesPessoais
informacoes = InformacoesPessoais()

# Chama a função ler_informacoes para ler a idade e a altura das pessoas
informacoes.ler_informacoes()

# Chama a função imprimir_informacoes_inverso para imprimir a idade e a altura na ordem inversa
informacoes.imprimir_informacoes_inverso()
