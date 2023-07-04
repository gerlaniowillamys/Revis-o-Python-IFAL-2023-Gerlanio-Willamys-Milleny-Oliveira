#Lista de Exercício 2 - Questão 23
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

class VerificarNumero:
    def __init__(self, num):
        self.num = num

    def verificar_inteiro_decimal(self):
        if self.num % 1 == 0:
            return "Inteiro"
        else:
            return "Decimal"


def main():
    try:
        num = float(input("Digite um número: "))
        verificar_numero = VerificarNumero(num)
        resultado = verificar_numero.verificar_inteiro_decimal()
        print(resultado)
    except ValueError:
        print("Valor inválido. Digite um número.")


if __name__ == "__main__":
    main()
