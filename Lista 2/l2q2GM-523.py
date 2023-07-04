#Lista de Exercício 2 - Questão 2
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def verificar_positivo_negativo(valor):
    if valor >= 0:
        return "positivo"
    else:
        return "negativo"

if __name__ == "__main__":
    try:
        valor = float(input("Digite um número: "))

        resultado = verificar_positivo_negativo(valor)

        print("O valor é", resultado)

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico válido.")
    except Exception as e:
        print("Ocorreu um erro:", e)
