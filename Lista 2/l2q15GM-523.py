#Lista de Exercício 2 - Questão 15
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def verificar_tipo(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if self.a == self.b and self.b == self.c:
                return "Triângulo Equilátero"
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                return "Triângulo Isósceles"
            else:
                return "Triângulo Escaleno"
        else:
            return "Não é possível formar um triângulo"


def main():
    a = float(input("Digite o valor do primeiro lado do triângulo: "))
    b = float(input("Digite o valor do segundo lado do triângulo: "))
    c = float(input("Digite o valor do terceiro lado do triângulo: "))

    triangulo = Triangulo(a, b, c)
    tipo_triangulo = triangulo.verificar_tipo()
    print(tipo_triangulo)


if __name__ == "__main__":
    main()
