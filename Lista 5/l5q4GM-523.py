#Lista de Exercício 5 - Questão 4
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verificar_positivo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

num = float(input("Insira um número: "))

resultado = verificar_positivo(num)

print(f"O número é {resultado}")