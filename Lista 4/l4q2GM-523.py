#Lista de Exercício 4 - Questão 2
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler um vetor de 10 números reais e mostrar os números na ordem inversa.

class VetorInverso:
    def __init__(self):
        self.vetor = []  # Lista vazia para armazenar os números reais

    def ler_vetor(self):
        # Função para ler os números reais e armazená-los no vetor
        try:
            for i in range(10):
                numero = float(input(f"Digite o número {i+1}: "))
                self.vetor.append(numero)
        except ValueError:
            print("Valor inválido. Por favor, digite um número real.")

    def mostrar_vetor_inverso(self):
        # Função para mostrar os números reais na ordem inversa
        print("Números na ordem inversa:")
        for numero in reversed(self.vetor):
            print(numero)

# Cria um objeto da classe VetorInverso
vetor_inverso = VetorInverso()

# Chama a função ler_vetor para ler os números
vetor_inverso.ler_vetor()

# Chama a função mostrar_vetor_inverso para mostrar os números na ordem inversa
vetor_inverso.mostrar_vetor_inverso()
