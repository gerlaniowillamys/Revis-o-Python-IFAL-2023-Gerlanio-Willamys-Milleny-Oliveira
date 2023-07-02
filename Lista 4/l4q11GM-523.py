#Lista de Exercício 4 - Questão 11
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Programa que lê três vetores com 10 elementos cada e gera um quarto vetor
# de 30 elementos com os valores intercalados dos três outros vetores.

class InterleavedVectors:
    def __init__(self):
        self.vector1 = []
        self.vector2 = []
        self.vector3 = []
        self.result_vector = []

    def read_vectors(self):
        # Função para ler os três vetores de 10 elementos cada.
        for i in range(10):
            try:
                element = int(input(f"Elemento do {i+1}º primeiro vetor: "))
                self.vector1.append(element)
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

        for i in range(10):
            try:
                element = int(input(f"Elemento do {i+1}º segundo vetor: "))
                self.vector2.append(element)
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

        for i in range(10):
            try:
                element = int(input(f"Elemento do {i+1}º terceiro vetor: "))
                self.vector3.append(element)
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

    def interleave_vectors(self):
        # Função para gerar o quarto vetor com os elementos intercalados dos três vetores.
        for i in range(10):
            self.result_vector.append(self.vector1[i])
            self.result_vector.append(self.vector2[i])
            self.result_vector.append(self.vector3[i])

    def display_result(self):
        # Função para exibir o quarto vetor gerado.
        print("Quarto vetor (resultante):")
        print(self.result_vector)


# Criando uma instância da classe InterleavedVectors
interleaved = InterleavedVectors()

# Lendo os vetores
interleaved.read_vectors()

# Gerando o quarto vetor
interleaved.interleave_vectors()

# Exibindo o resultado
interleaved.display_result()
