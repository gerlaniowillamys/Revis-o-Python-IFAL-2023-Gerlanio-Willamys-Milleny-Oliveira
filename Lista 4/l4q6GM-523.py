#Lista de Exercício 4 - Questão 6
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para calcular a média das notas de 10 alunos e imprimir o número de alunos com média maior ou igual a 7.0.

class CalculadoraMedia:
    def __init__(self):
        self.medias = []  # Lista vazia para armazenar as médias dos alunos

    def ler_notas(self):
        # Função para ler as notas de cada aluno e calcular a média
        try:
            for i in range(10):
                notas = []
                for j in range(4):
                    nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
                    notas.append(nota)

                media = sum(notas) / len(notas)
                self.medias.append(media)
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    def contar_alunos_aprovados(self):
        # Função para contar o número de alunos com média maior ou igual a 7.0
        count = 0
        for media in self.medias:
            if media >= 7.0:
                count += 1

        return count

# Cria um objeto da classe CalculadoraMedia
calculadora = CalculadoraMedia()

# Chama a função ler_notas para ler as notas dos alunos e calcular as médias
calculadora.ler_notas()

# Chama a função contar_alunos_aprovados para obter o número de alunos com média maior ou igual a 7.0
num_alunos_aprovados = calculadora.contar_alunos_aprovados()

# Imprime o número de alunos com média maior ou igual a 7.0
print("Número de alunos com média maior ou igual a 7.0:", num_alunos_aprovados)