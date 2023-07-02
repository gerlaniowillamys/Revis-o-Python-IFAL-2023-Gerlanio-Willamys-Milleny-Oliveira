#Lista de Exercício 3 - Questão 8
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler 5 números, calcular a soma e a média

class Numeros:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        # Solicita ao usuário que digite os números
        for i in range(5):
            while True:
                try:
                    numero = float(input("Digite um número: "))
                    self.numeros.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite apenas números.")

    def calcular_soma(self):
        # Calcula a soma dos números
        soma = sum(self.numeros)
        return soma

    def calcular_media(self):
        # Calcula a média dos números
        media = sum(self.numeros) / len(self.numeros)
        return media


def main():
    print("Programa para ler 5 números, calcular a soma e a média.\n")

    numeros = Numeros()
    numeros.ler_numeros()
    soma = numeros.calcular_soma()
    media = numeros.calcular_media()

    print("A soma dos números é:", soma)
    print("A média dos números é:", media)


if __name__ == '__main__':
    main()
