#Lista de Exercício 1 - Questão 10
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def converter_celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = converter_celsius_para_fahrenheit(celsius)
        print("A temperatura em graus Fahrenheit é:", fahrenheit)
    except ValueError:
        print("Entrada inválida. Por favor, digite uma temperatura válida em graus Celsius.")
    except Exception as e:
        print("Ocorreu um erro:", e)
