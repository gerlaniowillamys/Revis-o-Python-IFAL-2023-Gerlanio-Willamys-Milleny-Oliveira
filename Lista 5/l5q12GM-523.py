#Lista de Exercício 5 - Questão 12
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

class Embaralhador:
    def __init__(self, palavra):
        self.palavra = palavra

    def embaralhar_palavra(self):
        try:
            if not self.palavra:
                raise ValueError("A palavra não pode ser vazia.")

            caracteres = list(self.palavra.lower())

            random.shuffle(caracteres)

            palavra_embaralhada = ''.join(caracteres).upper()

            return palavra_embaralhada

        except ValueError as error:
            return str(error)


palavra = input("Digite uma palavra: ")
embaralhador = Embaralhador(palavra)
palavra_embaralhada = embaralhador.embaralhar_palavra()
print("Palavra embaralhada:", palavra_embaralhada)
