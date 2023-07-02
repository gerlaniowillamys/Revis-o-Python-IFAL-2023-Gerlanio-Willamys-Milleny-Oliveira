#Lista de Exercício 4 - Questão 24
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#lançamento do dado

import random

def lancamento_dados(n):
    resultados = []
    contadores = [0, 0, 0, 0, 0, 0]  # Vetor de contadores para cada valor do dado

    for _ in range(n):
        resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 simulando um lançamento de dado
        resultados.append(resultado)  # Armazena o resultado no vetor

        contadores[resultado - 1] += 1  # Incrementa o contador correspondente ao valor obtido

    return resultados, contadores

def main():
    num_lancamentos = 100

    resultados, contadores = lancamento_dados(num_lancamentos)

    print("Resultados dos lançamentos:")
    for i, resultado in enumerate(resultados):
        print(f"Lançamento {i+1}: {resultado}")

    print("\nQuantidade de vezes que cada valor foi obtido:")
    for i in range(6):
        print(f"Valor {i+1}: {contadores[i]} vezes")

if __name__ == "__main__":
    main()
