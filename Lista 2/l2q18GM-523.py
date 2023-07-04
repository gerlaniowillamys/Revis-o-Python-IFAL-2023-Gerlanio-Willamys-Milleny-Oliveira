#Lista de Exercício 2 - Questão 18
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

class VerificadorData:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def verificar_data(self):
        if self.dia < 1 or self.dia > 31:
            return False
        if self.mes < 1 or self.mes > 12:
            return False
        if self.mes == 2 and (self.dia > 29 or (self.dia == 29 and not self.verificar_ano_bissexto())):
            return False
        return True

    def verificar_ano_bissexto(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            return True
        return False


def main():
    try:
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))

        verificador = VerificadorData(dia, mes, ano)
        if verificador.verificar_data():
            print("DATA VÁLIDA.")
        else:
            print("DATA INVÁLIDA.")
    except ValueError:
        print("Valor inválido! Digite valores numéricos para dia, mês e ano.")


if __name__ == "__main__":
    main()
