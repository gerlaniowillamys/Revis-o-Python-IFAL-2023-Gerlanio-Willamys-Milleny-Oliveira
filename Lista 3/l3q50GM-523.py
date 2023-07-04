#Lista de Exercício 3 - Questão 50
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

def calcular_valor_H(n): #a função calcular_valor_H recebe o número de termos n como entrada e retorna o valor de H
    soma = 0
    for i in range(1, n+1):
        soma += 1 / i #Em cada iteração, adicionamos o valor de 1/i à soma
    return soma


def main(): #solicitamos ao usuário que digite o número de termos para calcular o valor de H
    try:
        n = int(input("Digite o número de termos para calcular H: "))
        if n <= 0:
            raise ValueError("O número de termos deve ser positivo.")

        valor_H = calcular_valor_H(n)
        print("Valor de H: ", valor_H)
    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()
