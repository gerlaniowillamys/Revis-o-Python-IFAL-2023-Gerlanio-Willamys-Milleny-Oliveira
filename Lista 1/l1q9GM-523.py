#Lista de Exercício 1 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

def converter_fahrenheit_para_celsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)

if __name__ == "__main__":
    try:
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = converter_fahrenheit_para_celsius(fahrenheit)
        print("A temperatura em graus Celsius é:", celsius)
    except ValueError:
        print("Entrada inválida. Por favor, digite uma temperatura válida em graus Fahrenheit.")
    except Exception as e:
        print("Ocorreu um erro:", e)
