#Lista de Exercício 2 - Questão 7
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia três números e mostre o maior e o menor deles.

def encontrar_maior_numero(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return None

def main():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        num3 = int(input("Digite o terceiro número: "))

        maior_numero = encontrar_maior_numero(num1, num2, num3)

        if maior_numero is not None:
            print("{} é o maior número.".format(maior_numero))
        else:
            print("Todos os números são iguais.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico válido para os números.")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()
