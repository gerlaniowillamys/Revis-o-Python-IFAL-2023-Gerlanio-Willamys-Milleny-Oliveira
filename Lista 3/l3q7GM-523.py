#Lista de Exercício 3 - Questão 7
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para encontrar o maior número dentre 5 números digitados pelo usuário

class Numeros:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        # Lê os números digitados pelo usuário
        for i in range(5):
            while True:
                try:
                    numero = float(input("Digite um número: "))
                    self.numeros.append(numero)
                    break
                except ValueError:
                    print("Valor inválido. Digite apenas números.")

    def encontrar_maior_numero(self):
        # Encontra o maior número dentre os números digitados
        maior_numero = max(self.numeros)
        return maior_numero


def main():
    print("Programa para encontrar o maior número dentre 5 números.\n")

    numeros = Numeros()
    numeros.ler_numeros()
    maior_numero = numeros.encontrar_maior_numero()

    print("O maior número é:", maior_numero)


if __name__ == '__main__':
    main()
