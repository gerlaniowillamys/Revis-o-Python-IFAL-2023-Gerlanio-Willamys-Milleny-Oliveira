#Lista de Exercício 3 - Questão 39
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para encontrar o aluno mais alto e o mais baixo com base em conjuntos de valores.

#O programa lê dez conjuntos de dois valores: o número do aluno e a sua altura em centímetros.
#Em seguida, encontra o aluno mais alto e o mais baixo e exibe seus números e alturas.

def encontrar_aluno_mais_alto_baixo():
    aluno_mais_alto = None
    aluno_mais_baixo = None

    for i in range(1, 11):
        try:
            numero_aluno = int(input(f"Número do aluno {i}: "))
            altura = float(input(f"Altura (em centímetros) do aluno {i}: "))

            if aluno_mais_alto is None or altura > aluno_mais_alto[1]:
                aluno_mais_alto = (numero_aluno, altura)

            if aluno_mais_baixo is None or altura < aluno_mais_baixo[1]:
                aluno_mais_baixo = (numero_aluno, altura)

        except ValueError:
            print("Valor inválido. Tente novamente.")

    return aluno_mais_alto, aluno_mais_baixo

if __name__ == "__main__":
    aluno_mais_alto, aluno_mais_baixo = encontrar_aluno_mais_alto_baixo()

    print(f"Aluno mais alto: Número {aluno_mais_alto[0]}, Altura {aluno_mais_alto[1]} cm")
    print(f"Aluno mais baixo: Número {aluno_mais_baixo[0]}, Altura {aluno_mais_baixo[1]} cm")
