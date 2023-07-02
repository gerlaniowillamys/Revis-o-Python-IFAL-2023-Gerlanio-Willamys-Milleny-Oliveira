#Lista de Exercício 3 - Questão 16
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para gerar a série de Fibonacci até que o valor seja maior que 500

class GeradorFibonacci:
    def gerar_serie_fibonacci(self):
        # Casos base para a série de Fibonacci
        fibonacci = [0, 1]

        # Gera a série de Fibonacci até que o valor seja maior que 500
        while fibonacci[-1] <= 500:
            proximo = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(proximo)

        return fibonacci

def main():
    print("Gerador da Série de Fibonacci\n")

    try:
        # Cria um objeto do gerador de Fibonacci e chama a função para gerar a série
        gerador = GeradorFibonacci()
        serie_fibonacci = gerador.gerar_serie_fibonacci()

        # Exibe a série de Fibonacci
        print("Série de Fibonacci até que o valor seja maior que 500:")
        for numero in serie_fibonacci:
            print(numero, end=" ")

    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
