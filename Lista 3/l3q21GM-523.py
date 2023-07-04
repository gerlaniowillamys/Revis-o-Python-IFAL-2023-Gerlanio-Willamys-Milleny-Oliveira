#Lista de Exercício 3 - Questão 21
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe responsável por realizar as operações relacionadas a números primos
class VerificadorPrimo:
    def eh_primo(self, numero):
        # Verifica se o número é menor que 2
        if numero < 2:
            return False

        # Verifica se o número é divisível por algum número entre 2 e a sua raiz quadrada
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False

        # Caso não seja divisível por nenhum número, é primo
        return True


def main():
    print("Verificador de Números Primos\n")

    try:
        # Solicita ao usuário um número inteiro
        numero = int(input("Digite um número inteiro: "))

        # Cria um objeto da classe VerificadorPrimo e verifica se o número é primo
        verificador = VerificadorPrimo()
        if verificador.eh_primo(numero):
            print(f"O número {numero} é primo.")
        else:
            print(f"O número {numero} não é primo.")

    except ValueError:
        print("Erro: Valor inválido. Digite um número inteiro.")

    except Exception as e:
        print("Ocorreu um erro:", str(e))


if __name__ == '__main__':
    main()