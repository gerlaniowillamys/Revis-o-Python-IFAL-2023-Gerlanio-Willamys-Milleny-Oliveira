#Lista de Exercício 3 - Questão 17
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para calcular o fatorial de um número inteiro e exibir o resultado no formato desejado

class CalculadoraFatorial:
    def calcular_fatorial(self, n):
        # Verifica se o número é negativo
        if n < 0:
            raise ValueError("O número deve ser não negativo.")

        # Caso base: fatorial de 0 é 1
        if n == 0:
            return 1

        # Calcula o fatorial iterativamente
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i

        return fatorial

def main():
    print("Calculadora de Fatorial\n")

    try:
        # Solicita o número para cálculo do fatorial
        numero = int(input("Digite um número inteiro: "))

        # Cria um objeto da calculadora de fatorial e chama a função para calcular o fatorial
        calculadora = CalculadoraFatorial()
        fatorial = calculadora.calcular_fatorial(numero)

        # Monta a representação do fatorial no formato desejado
        fatorial_str = ".".join(str(i) for i in range(numero, 0, -1))
        fatorial_repr = f"{numero}! = {fatorial_str} = {fatorial}"

        # Exibe o resultado
        print(fatorial_repr)

    except ValueError as ve:
        print("Erro:", str(ve))
    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
