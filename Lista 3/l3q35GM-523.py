#Lista de Exercício 3 - Questão 35
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para gerar uma lista de números primos.

#O programa recebe um número inteiro do usuário e gera uma lista com todos os números primos entre 1 e o número informado.


class GeradorPrimos:
    def __init__(self, limite):
        self.limite = limite

    def gerar_primos(self):
        primos = []

        for num in range(2, self.limite + 1):
            is_primo = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_primo = False
                    break

            if is_primo:
                primos.append(num)

        return primos

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))

        gerador = GeradorPrimos(numero)

        lista_primos = gerador.gerar_primos()

        if len(lista_primos) > 0:
            print("Números primos encontrados:")
            for primo in lista_primos:
                print(primo)
        else:
            print("Não foram encontrados números primos no intervalo.")

    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

