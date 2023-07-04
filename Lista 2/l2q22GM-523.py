#Lista de Exercício 2 - Questão 22
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

class ParImpar:
    def __init__(self, num):
        self.num = num

    def verificar_par_impar(self):
        if self.num % 2 == 0:
            return "Par"
        else:
            return "Ímpar"


def main():
    try:
        num = int(input("Digite um número: "))
        par_impar = ParImpar(num)
        resultado = par_impar.verificar_par_impar()
        print(resultado)
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")


if __name__ == "__main__":
    main()
