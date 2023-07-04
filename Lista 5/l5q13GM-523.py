#Lista de Exercício 5 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

class Moldura:
    def __init__(self, linhas=1, colunas=1):
        self.linhas = linhas
        self.colunas = colunas

    def desenhar_moldura(self):
        try:
            if self.linhas < 1 or self.linhas > 20:
                self.linhas = max(1, min(self.linhas, 20))
            if self.colunas < 1 or self.colunas > 20:
                self.colunas = max(1, min(self.colunas, 20))

            print('+' + '-' * self.colunas + '+')
            for _ in range(self.linhas):
                print('|' + ' ' * self.colunas + '|')
            print('+' + '-' * self.colunas + '+')

        except ValueError as error:
            return str(error)


linhas = int(input("Digite o número de linhas (1 a 20): "))
colunas = int(input("Digite o número de colunas (1 a 20): "))

moldura = Moldura(linhas, colunas)
moldura.desenhar_moldura()
