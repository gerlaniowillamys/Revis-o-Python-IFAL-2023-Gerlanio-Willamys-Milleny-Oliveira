#Lista de Exercício 5 - Questão 11
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

class DataExtensor:
    def __init__(self, data):
        self.data = data

    def obter_data_extenso(self):
        try:
            if len(self.data) != 10 or self.data[2] != '/' or self.data[5] != '/':
                raise ValueError("Formato de data inválido.")

            dia, mes, ano = self.data.split('/')

            if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
                raise ValueError("A data deve conter apenas números.")

            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            meses_extenso = {
                1: 'janeiro',
                2: 'fevereiro',
                3: 'março',
                4: 'abril',
                5: 'maio',
                6: 'junho',
                7: 'julho',
                8: 'agosto',
                9: 'setembro',
                10: 'outubro',
                11: 'novembro',
                12: 'dezembro'
            }

            if mes < 1 or mes > 12:
                raise ValueError("Mês inválido.")

            if dia < 1 or dia > 31:
                raise ValueError("Dia inválido.")

            if mes == 2:
                if dia > 29:
                    raise ValueError("Dia inválido para o mês de fevereiro.")
                elif dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
                    raise ValueError("Dia inválido para o ano bissexto.")
            elif mes in [4, 6, 9, 11]:
                if dia > 30:
                    raise ValueError("Dia inválido para o mês selecionado.")

            data_extenso = f"{dia} de {meses_extenso[mes]} de {ano}"
            return data_extenso

        except ValueError as error:
            return str(error)


data = input("Digite a data no formato DD/MM/AAAA: ")
extensor = DataExtensor(data)
data_extenso = extensor.obter_data_extenso()
print(data_extenso)
