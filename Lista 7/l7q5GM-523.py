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
        self._numero_conta = numero_conta
        self._nome_correntista = nome_correntista
        self._saldo = saldo

    def alterarNome(self, novo_nome):
        self._nome_correntista = novo_nome

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor

    def saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor

    def mostrarInformacoes(self):
        return "Número da conta: {}, Nome do correntista: {}, Saldo: {}".format(self._numero_conta, self._nome_correntista, self._saldo)

# Exemplo de uso da classe ContaCorrente
try:
    conta = ContaCorrente("1206", "GM")
    print(conta.mostrarInformacoes())
    conta.alterarNome("MG")
    conta.deposito(1000)
    conta.saque(500)
    print(conta.mostrarInformacoes())
except ValueError as error:
    print("Erro:", str(error))
