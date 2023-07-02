#Lista de Exercício 3 - Questão 15
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para gerar a série de Fibonacci até o n-ésimo termo

class GeradorFibonacci:
    def gerar_serie_fibonacci(self, n):
        # Verifica se n é válido
        if n <= 0:
            raise ValueError("O valor de n deve ser um número inteiro positivo.")

        # Casos base para n = 1 e n = 2
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 1]

        # Gera a série de Fibonacci
        fibonacci = [1, 1]
        while len(fibonacci) < n:
            proximo = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(proximo)

        return fibonacci

def main():
    print("Gerador da Série de Fibonacci\n")

    try:
        # Solicita a entrada do valor de n
        n = int(input("Digite o valor de n: "))

        # Cria um objeto do gerador de Fibonacci e chama a função para gerar a série
        gerador = GeradorFibonacci()
        serie_fibonacci = gerador.gerar_serie_fibonacci(n)

        # Exibe a série de Fibonacci
        print("\nSérie de Fibonacci até o", n, "° termo:")
        for numero in serie_fibonacci:
            print(numero, end=" ")

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar um número inteiro positivo.")

    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
