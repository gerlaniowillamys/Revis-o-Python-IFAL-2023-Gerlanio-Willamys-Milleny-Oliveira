#Lista de Exercício 2 - Questão 1 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça dois números e imprima o maior deles.

def encontrar_maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

if __name__ == "__main__":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        maior_numero = encontrar_maior_numero(num1, num2)

        print("O maior número é:", maior_numero)

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos válidos para os números.")
    except Exception as e:
        print("Ocorreu um erro:", e)
