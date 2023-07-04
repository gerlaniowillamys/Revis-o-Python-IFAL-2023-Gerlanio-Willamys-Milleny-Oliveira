#Lista de Exercício 7 - Questão 12
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicione_juros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)

# Exemplo de uso da classe

# Criando uma instância da classe ContaInvestimento
poupanca = ContaInvestimento(1000.00, 10.0)  # Saldo inicial de R$1000,00 e taxa de juros de 10%.

# Aplicando o método adicione_juros() cinco vezes
for _ in range(5):
    poupanca.adicione_juros()

# Obtendo o saldo resultante
saldo_resultante = poupanca.saldo
print(f"Saldo resultante: R${saldo_resultante:.2f}")
