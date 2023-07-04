#Lista de Exercício 2 - Questão 14
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E

class Nota:
    def __init__(self, valor):
        self.valor = valor

    def calcular_conceito(self):
        if self.valor >= 9:
            return "A"
        elif self.valor >= 7.5:
            return "B"
        elif self.valor >= 6:
            return "C"
        elif self.valor >= 4:
            return "D"
        else:
            return "E"

def obter_nota():
    while True:
        try:
            valor = float(input("Digite a nota: "))
            return Nota(valor)
        except ValueError:
            print("Valor inválido. Digite novamente.")

nota1 = obter_nota()
nota2 = obter_nota()

media = (nota1.valor + nota2.valor) / 2
conceito = nota1.calcular_conceito()

if conceito == "E":
    print("Conceito: E - REPROVADO!")
else:
    print("Conceito: {} - APROVADO!".format(conceito))
