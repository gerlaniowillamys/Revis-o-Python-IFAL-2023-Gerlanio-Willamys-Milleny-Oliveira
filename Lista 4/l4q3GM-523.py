#Lista de Exercício 4 - Questão 3
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


# Programa para ler 4 notas, mostrar as notas e calcular a média.

class CalculadoraNotas:
    def __init__(self):
        self.notas = []  # Lista vazia para armazenar as notas

    def ler_notas(self):
        # Função para ler as notas e armazená-las na lista
        try:
            for i in range(4):
                nota = float(input(f"Digite a nota {i+1}: "))
                self.notas.append(nota)
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    def mostrar_notas(self):
        # Função para mostrar as notas
        print("Notas digitadas:")
        for nota in self.notas:
            print(nota)

    def calcular_media(self):
        # Função para calcular a média das notas
        if len(self.notas) == 0:
            print("Não há notas para calcular a média.")
            return

        soma = sum(self.notas)
        media = soma / len(self.notas)
        print("Média das notas:", media)

# Cria um objeto da classe CalculadoraNotas
calculadora = CalculadoraNotas()

# Chama a função ler_notas para ler as notas
calculadora.ler_notas()

# Chama a função mostrar_notas para mostrar as notas
calculadora.mostrar_notas()

# Chama a função calcular_media para calcular a média das notas
calculadora.calcular_media()
 

