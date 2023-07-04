#Lista de Exercício 2 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros


def main():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        num3 = int(input("Digite o terceiro número: "))

        numeros_ordenados = ordenar_numeros(num1, num2, num3)

        if num1 == num2 == num3:
            print("Os números são iguais.")
        else:
            print("\n".join(str(num) for num in numeros_ordenados))
    except ValueError:
        print("Valores inválidos. Certifique-se de digitar números inteiros.")


if __name__ == "__main__":
    main()
