#Lista de Exercício 2 - Questão 11
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Digite seu salário (R$): "))

if (salario <= 280):
    aumento = ((20*salario)/100)
    salarioF = aumento + salario
    print("Seu salário é  de: R${}".format(salario))
    print("Percentual almentado: 20%")
    print("O aumento foi de: R${}".format(aumento))
    print("O Salário final é de: R${}".format(salarioF))

elif (salario > 280 and salario < 700):
    aumento = ((15*salario)/100)
    salarioF = aumento + salario
    print("Seu salário é  de: R${}".format(salario))
    print("Percentual almentado: 15%")
    print("O aumento foi de: R${}".format(aumento))
    print("O Salário final é de: R${}".format(salarioF))

elif (salario >= 700 and salario < 1500):
    aumento = ((10*salario)/100)
    salarioF = aumento + salario
    print("Seu salário é  de: R${}".format(salario))
    print("Percentual almentado: 10%")
    print("O aumento foi de: R${}".format(aumento))
    print("O Salário final é de: R${}".format(salarioF))

elif (salario >= 1500):
    aumento = ((5*salario)/100)
    salarioF = aumento + salario
    print("Seu salário é  de: R${}".format(salario))
    print("Percentual almentado: 5%")
    print("O aumento foi de: R${}".format(aumento))
    print("O Salário final é de: R${}".format(salarioF))