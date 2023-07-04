#Lista de Exercício 1 - Questão 3 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça dois números e imprima a soma.

def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def somar_numeros(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    try:
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        soma = somar_numeros(num1, num2)

        print("A soma dos números é:", soma)
    except Exception as e:
        print("Ocorreu um erro:", e)
