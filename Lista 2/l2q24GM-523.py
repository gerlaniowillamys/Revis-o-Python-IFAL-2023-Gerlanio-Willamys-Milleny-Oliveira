#Lista de Exercício 2 - Questão 24
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

def realizar_operacao(numero1, numero2, operacao):
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else:
        raise ValueError("Operação inválida")

    return resultado


def verificar_tipo_numero(numero):
    if numero // 1 == numero:
        print("Inteiro")
        if numero % 2 == 0:
            print("Par")
            if numero > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Ímpar")
    else:
        print("Decimal")


def main():
    try:
        numero1 = float(input("Digite o número 1: "))
        numero2 = float(input("Digite o número 2: "))
        operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")

        resultado = realizar_operacao(numero1, numero2, operacao)
        print("Resultado:", resultado)

        verificar_tipo_numero(resultado)
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
