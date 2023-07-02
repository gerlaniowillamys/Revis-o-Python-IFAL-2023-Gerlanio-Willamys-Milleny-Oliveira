#Lista de Exercício 7 - Questão 14
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


class Funcionario:
    def __init__(self, nome, salario):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        if not isinstance(salario, float) and not isinstance(salario, int):
            raise TypeError("O salário deve ser um número")
        if salario < 0:
            raise ValueError("O salário não pode ser negativo")

        self.nome = nome
        self.salario = float(salario)

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        if not isinstance(porcentualDeAumento, float) and not isinstance(porcentualDeAumento, int):
            raise TypeError("O porcentual de aumento deve ser um número")
        if porcentualDeAumento < 0:
            raise ValueError("O porcentual de aumento não pode ser negativo")

        aumento = self.salario * porcentualDeAumento / 100
        self.salario += aumento


# Testando a classe Funcionario
try:
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = Funcionario(nome, salario)
    print("Nome:", funcionario.get_nome())
    print("Salário:", funcionario.get_salario())

    porcentual = float(input("Digite o porcentual de aumento do salário: "))
    funcionario.aumentarSalario(porcentual)

    print("Novo salário:", funcionario.get_salario())
except ValueError as e:
    print("Erro:", e)
except TypeError as e:
    print("Erro:", e)