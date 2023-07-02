#Lista de Exercício 5 - Questão 12
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

def embaralhar_palavra(palavra):
    palavra = palavra.lower()

    caracteres = list(palavra)

    random.shuffle(caracteres)

    palavra_embaralhada = ''.join(caracteres)

    return palavra_embaralhada.upper()

palavra = input("Digite uma palavra: ")
palavra_embaralhada = embaralhar_palavra(palavra)
print("Palavra embaralhada:", palavra_embaralhada)
