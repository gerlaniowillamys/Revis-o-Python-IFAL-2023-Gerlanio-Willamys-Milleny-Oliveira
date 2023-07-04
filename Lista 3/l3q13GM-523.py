#Lista de Exercício 3 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para calcular a potência de um número

class CalculadoraPotencia:
    def calcular_potencia(self, base, expoente):
        # Verifica se o expoente é negativo
        if expoente < 0:
            raise ValueError("O expoente deve ser um número não negativo.")

        resultado = 1

        # Calcula a potência iterativamente
        for _ in range(expoente):
            resultado *= base

        return resultado

def main():
    print("Calculadora de Potência\n")

    try:
        # Solicita a entrada da base e do expoente
        base = float(input("Digite a base: "))
        expoente = int(input("Digite o expoente: "))

        # Cria um objeto da calculadora de potência e chama a função para calcular a potência
        calculadora = CalculadoraPotencia()
        potencia = calculadora.calcular_potencia(base, expoente)

        # Exibe o resultado da potência
        print(f"\n{base} elevado a {expoente} é igual a {potencia}")

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números válidos.")

    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
