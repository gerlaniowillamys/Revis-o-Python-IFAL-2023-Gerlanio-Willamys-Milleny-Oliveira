#Lista de Exercício 7 - Questão 10
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Bomba de Combustível: Programa que simula uma bomba de combustível com os atributos e métodos especificados.


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        try:
            litros_abastecidos = valor / self.valor_litro
            if litros_abastecidos <= self.quantidade_combustivel:
                self.quantidade_combustivel -= litros_abastecidos
                print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")
            else:
                print("Não há combustível suficiente na bomba.")
        except ZeroDivisionError:
            print("Valor do litro do combustível não pode ser zero.")

    def abastecer_por_litro(self, litros):
        try:
            valor_pagar = litros * self.valor_litro
            if litros <= self.quantidade_combustivel:
                self.quantidade_combustivel -= litros
                print(f"Valor a ser pago: R$ {valor_pagar:.2f}")
            else:
                print("Não há combustível suficiente na bomba.")
        except ZeroDivisionError:
            print("Valor do litro do combustível não pode ser zero.")

    def alterar_valor(self, novo_valor):
        try:
            self.valor_litro = novo_valor
            print("Valor do litro do combustível alterado com sucesso.")
        except ValueError:
            print("Valor inválido.")

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        print("Tipo do combustível alterado com sucesso.")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print("Quantidade de combustível alterada com sucesso.")


# Exemplo de uso da classe

# Criando uma instância da classe BombaCombustivel
bomba = BombaCombustivel("Gasolina", 4.89, 500)

# Abastecendo por valor
bomba.abastecer_por_valor(100)  # Exemplo: abastecer R$ 100

# Abastecendo por litro
bomba.abastecer_por_litro(20)  # Exemplo: abastecer 20 litros
