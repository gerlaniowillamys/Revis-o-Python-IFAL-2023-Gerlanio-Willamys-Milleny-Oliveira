#Lista de Exercício 7 - Questão 5
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


# Classe Conta Corrente: Faça um programa que crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque.
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor

    def saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor

# Exemplo de uso da classe ContaCorrente
try:
    conta = ContaCorrente("1206", "GM")
    print("Número da conta:", conta.numero_conta)
    print("Nome do correntista:", conta.nome_correntista)
    print("Saldo:", conta.saldo)
    conta.alterarNome("MG")
    conta.deposito(1000)
    conta.saque(500)
    print("Nome do correntista após alteração:", conta.nome_correntista)
    print("Saldo após depósito e saque:", conta.saldo)
except ValueError as error:
    print("Erro:", str(error))
