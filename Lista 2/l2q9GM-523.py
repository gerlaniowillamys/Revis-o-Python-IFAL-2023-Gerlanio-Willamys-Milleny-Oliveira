#Lista de Exercício 2 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 > num2 and num2 > num3):
    print("{}\n{}\n{}\n".format(num1,num2,num3))

elif (num2 > num1 and num1 > num3):
    print("{}\n{}\n{}\n".format(num2,num1,num3))

elif (num1 > num3 and num3 > num2):
    print("{}\n{}\n{}\n".format(num1,num3,num2))

elif (num3 > num1 and num1 > num2):
    print("{}\n{}\n{}\n".format(num3,num1,num2))

elif (num2 > num3 and num3 > num1):
    print("{}\n{}\n{}\n".format(num2,num3,num1))

elif (num3 > num2 and num2 > num1):
    print("{}\n{}\n{}\n".format(num3,num2,num1))

else:
    print("Os números são iguais.")