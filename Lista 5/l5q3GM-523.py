#Lista de Exercício 5 - Questão 3
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

class Calculadora:
    @staticmethod
    def soma_tres_numeros(a, b, c):
        return a + b + c

    @classmethod
    def ler_e_calcular_soma(cls):
        try:
            num1 = int(input("Insira o primeiro número: "))
            num2 = int(input("Insira o segundo número: "))
            num3 = int(input("Insira o terceiro número: "))

            resultado = cls.soma_tres_numeros(num1, num2, num3)

            print(f"A soma dos três números é {resultado}")
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números inteiros.")

Calculadora.ler_e_calcular_soma()
