#Lista de Exercício 3 - Questão 11
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para gerar os números inteiros dentro de um intervalo e calcular a soma

def gerar_numeros_inteiros(inicio, fim):
    # Verifica se os números fornecidos estão em ordem crescente
    if inicio > fim:
        inicio, fim = fim, inicio

    # Gera e imprime os números inteiros no intervalo
    numeros = []
    for numero in range(inicio + 1, fim):
        numeros.append(numero)
        print(numero, end=' ')

    return numeros

def calcular_soma(numeros):
    # Calcula a soma dos números
    soma = sum(numeros)
    return soma

def main():
    print("Programa para gerar os números inteiros dentro de um intervalo e calcular a soma.\n")

    try:
        # Solicita a entrada dos números
        inicio = int(input("Digite o primeiro número: "))
        fim = int(input("Digite o segundo número: "))

        # Gera os números inteiros
        numeros = gerar_numeros_inteiros(inicio, fim)

        # Calcula a soma dos números
        soma = calcular_soma(numeros)

        # Exibe a soma dos números
        print("\nSoma dos números:", soma)

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar apenas números inteiros.")

if __name__ == '__main__':
    main()
