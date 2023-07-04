#Lista de Exercício 3 - Questão 41
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

def contar_intervalos():
    intervalos = [0, 0, 0, 0]  # [0-25], [26-50], [51-75], [76-100]

    while True:
        numero = int(input("Digite um número positivo (ou negativo para sair): "))
        if numero < 0:
            break

        if 0 <= numero <= 25:
            intervalos[0] += 1
        elif 26 <= numero <= 50:
            intervalos[1] += 1
        elif 51 <= numero <= 75:
            intervalos[2] += 1
        elif 76 <= numero <= 100:
            intervalos[3] += 1

    print(f"Quantidade de números no intervalo [0-25]: {intervalos[0]}")
    print(f"Quantidade de números no intervalo [26-50]: {intervalos[1]}")
    print(f"Quantidade de números no intervalo [51-75]: {intervalos[2]}")
    print(f"Quantidade de números no intervalo [76-100]: {intervalos[3]}")


# Exemplo de uso
contar_intervalos()
