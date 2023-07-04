#Lista de Exercício 3 - Questão 14
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para contar números pares e ímpares

class ContadorParesImpares:
    def contar_pares_impares(self, numeros):
        quantidade_pares = 0
        quantidade_impares = 0

        # Itera sobre os números e verifica se são pares ou ímpares
        for numero in numeros:
            if numero % 2 == 0:
                quantidade_pares += 1
            else:
                quantidade_impares += 1

        return quantidade_pares, quantidade_impares

def main():
    print("Contador de Números Pares e Ímpares\n")

    try:
        numeros = []

        # Solicita a entrada dos 10 números inteiros
        for i in range(10):
            numero = int(input(f"Digite o número {i+1}: "))
            numeros.append(numero)

        # Cria um objeto do contador de pares e ímpares e chama a função para contar
        contador = ContadorParesImpares()
        pares, impares = contador.contar_pares_impares(numeros)

        # Exibe o resultado
        print("\nQuantidade de números pares:", pares)
        print("Quantidade de números ímpares:", impares)

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar apenas números inteiros.")

    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
