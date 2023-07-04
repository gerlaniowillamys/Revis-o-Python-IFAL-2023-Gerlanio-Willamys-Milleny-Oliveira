#Lista de Exercício 3 - Questão 51
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#o número de termos da série como entrada e retorna a soma da série.
def calcular_serie(n):
    soma = 0 #Inicializamos a variável soma como zero e a variável m como 1.
    m = 1
    for i in range(1, n+1): #usamos um loop for para iterar de 1 a n e calcular cada termo da série.
        termo = i / m
        soma += termo
        m += 2
    return soma


def main(): #solicitamos ao usuário que digite o número de termos da série.
    try:
        n = int(input("Digite o número de termos da série: "))
        if n <= 0:
            raise ValueError("O número de termos deve ser positivo.")

        resultado = calcular_serie(n)
        print("S: ")
        for i in range(1, n+1):
            termo = f"{i}/{2*i-1}"
            print(termo, end=" ")
            if i != n:
                print("+", end=" ")
            else:
                print()
        print("Soma da série:", resultado)
    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()
