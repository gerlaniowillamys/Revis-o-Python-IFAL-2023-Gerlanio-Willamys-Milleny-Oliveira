#Lista de Exercício 5 - Questão 11
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def obter_data_extenso(data):
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return "NULL"

    dia, mes, ano = data.split('/')

    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        return "NULL"

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
        return "NULL"

    if dia < 1 or dia > 31:
        return "NULL"

    if mes == 2:
        if dia > 29:
            return "NULL"
        elif dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
            return "NULL"
    elif mes in [4, 6, 9, 11]:
        if dia > 30:
            return "NULL"

    data_extenso = f"{dia} de {meses_extenso[mes]} de {ano}"
    return data_extenso

data = input("Digite a data no formato DD/MM/AAAA: ")
data_extenso = obter_data_extenso(data)
print(data_extenso)
