#Lista de Exercício 3 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para imprimir os números ímpares entre 1 e 50

class NumerosImpares:
    def imprimir_impares(self):
        # Imprime os números ímpares entre 1 e 50
        for numero in range(1, 51):
            if numero % 2 != 0:
                print(numero)

def main():
    print("Programa para imprimir os números ímpares entre 1 e 50.\n")

    impares = NumerosImpares()
    impares.imprimir_impares()

if __name__ == '__main__':
    main()
