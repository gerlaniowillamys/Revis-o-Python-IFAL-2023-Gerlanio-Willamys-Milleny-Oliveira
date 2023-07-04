#Lista de Exercício 7 - Questão 13
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Funcionario possui um construtor __init__ que recebe dois parâmetros: nome (uma string) e salario (um número)
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
		#Os métodos get_nome e get_salario retornam o nome e o salário do funcionário, respectivamente.
    def get_salario(self):
        return self.salario


# Testando a classe Funcionario
try:
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = Funcionario(nome, salario)
    print("Nome:", funcionario.get_nome())
    print("Salário:", funcionario.get_salario())
except ValueError as e:
    print("Erro:", e)
except TypeError as e:
    print("Erro:", e)
