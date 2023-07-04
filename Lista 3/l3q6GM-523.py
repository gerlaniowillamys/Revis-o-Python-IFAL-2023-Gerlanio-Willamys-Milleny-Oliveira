#Lista de Exercício 3 - Questão 6
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe responsável por imprimir os números de 1 a 20 abaixo e lado a lado
class Numeros:
    def imprimir_numeros_abaixo(self):
        # Imprime os números de 1 a 20 um abaixo do outro
        for i in range(1, 21):
            print(i)

    def imprimir_numeros_lado(self):
        # Imprime os números de 1 a 20 lado a lado
        for i in range(1, 21):
            print(i, end=" ")


# Classe responsável por interagir com o usuário e obter a opção selecionada
class Menu:
    def obter_opcao(self):
        while True:
            opcao = input("Selecione uma opção:\n1 - Imprimir números abaixo\n2 - Imprimir números lado a lado\n")

            try:
                opcao = int(opcao)
                if opcao in (1, 2):
                    return opcao
                else:
                    print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Opção inválida. Digite um número inteiro.")


def main():
    print("Programa para imprimir números de 1 a 20 abaixo e lado a lado.\n")

    numeros = Numeros()
    menu = Menu()

    opcao = menu.obter_opcao()

    if opcao == 1:
        numeros.imprimir_numeros_abaixo()
    elif opcao == 2:
        numeros.imprimir_numeros_lado()


if __name__ == '__main__':
    main()
