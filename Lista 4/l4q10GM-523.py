#Lista de Exercício 4 - Questão 10
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para intercalar elementos de dois vetores

class VetorIntercale:
    def __init__(self):
        self.vetor1 = []
        self.vetor2 = []

    def ler_vetores(self):
        try:
            print("Elementos do primeiro vetor")
            for i in range(10):
                elemento = int(input(f"Elemento {i+1}: "))
                self.vetor1.append(elemento)

            print("Elementos do segundo vetor")
            for i in range(10):
                elemento = int(input(f"Elemento {i+1}: "))
                self.vetor2.append(elemento)

        except ValueError:
            print("Erro: Valor inválido. Certifique-se de digitar um número inteiro.")

    def intercalar_vetores(self):
        vetor_intercalado = []
        for i in range(10):
            vetor_intercalado.append(self.vetor1[i])
            vetor_intercalado.append(self.vetor2[i])

        return vetor_intercalado

    def imprimir_vetor_intercalado(self, vetor_intercalado):
        print("Vetor intercalado:")
        print(vetor_intercalado)


def main():
    vetor_intercale = VetorIntercale()
    vetor_intercale.ler_vetores()
    vetor_intercalado = vetor_intercale.intercalar_vetores()
    vetor_intercale.imprimir_vetor_intercalado(vetor_intercalado)


if __name__ == "__main__":
    main()
