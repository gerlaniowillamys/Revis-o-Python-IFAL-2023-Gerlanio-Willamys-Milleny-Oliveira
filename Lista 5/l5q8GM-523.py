#Lista de Exercício 5 - Questão 8
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contar_digitos(numero):
    return len(str(numero))

num = int(input("Insira um número inteiro: "))

qtd_digitos = contar_digitos(num)

print(f"O número {num} tem {qtd_digitos} dígitos")