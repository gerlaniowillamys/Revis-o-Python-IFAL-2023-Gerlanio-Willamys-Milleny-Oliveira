#Lista de Exercício 5 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    numero_str = str(numero)
    reverso_str = numero_str[::-1]
    return int(reverso_str)

numero = int(input("Insira um número inteiro: "))
reverso_num = reverso(numero)

print(f"O reverso de {numero} é {reverso_num}")