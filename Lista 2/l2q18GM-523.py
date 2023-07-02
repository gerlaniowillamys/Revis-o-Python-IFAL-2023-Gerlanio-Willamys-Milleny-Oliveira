#Lista de Exercício 2 - Questão 18
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

print("{}/{}/{}".format(dia,mes,ano))

if (dia < 1 or dia  > 31):
    print("DATA INVÁLIDA.")

elif (mes < 1 or mes > 12):
    print("DATA INVÁLIDA.")

elif (mes == 2 and dia > 29):
    print("DATA INVÁLIDA.")

else:
    print("DATA VÁLIDA.")