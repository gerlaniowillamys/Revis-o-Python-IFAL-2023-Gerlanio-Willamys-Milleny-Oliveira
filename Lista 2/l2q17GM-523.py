#Lista de Exercício 2 - Questão 17
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

class VerificadorAnoBissexto:
    def __init__(self, ano):
        self.ano = ano

    def verificar_bissexto(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            return True
        else:
            return False


def main():
    try:
        ano = int(input("Digite um ano qualquer: "))
        verificador = VerificadorAnoBissexto(ano)
        if verificador.verificar_bissexto():
            print("O ano é bissexto.")
        else:
            print("O ano não é bissexto.")
    except ValueError:
        print("Valor inválido! Digite um ano válido.")


if __name__ == "__main__":
    main()
