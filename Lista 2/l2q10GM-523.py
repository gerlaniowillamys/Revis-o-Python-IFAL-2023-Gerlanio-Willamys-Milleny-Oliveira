#Lista de Exercício 2 - Questão 10
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("[M]Matutino\n[V]Vespertino\n[N]Noturno\nDigite seu turno : ")

if (turno.lower() == "m"):
    print("Bom dia!")

elif (turno.lower() == "v"):
    print("Boa tarde!")

elif (turno.lower() == "n"):
    print("Boa noite!")

else:
    print("Turno inválido.")