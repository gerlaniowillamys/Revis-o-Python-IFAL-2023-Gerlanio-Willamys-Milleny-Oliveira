#Lista de Exercício 3 - Questão 31
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa da caixa registradora para a loja de conveniências.

#O programa recebe os preços das mercadorias até que seja informado um valor zero.

#Em seguida, calcula o total da compra, solicita o valor em dinheiro fornecido pelo cliente e calcula o troco.

#Após essa operação, o programa reinicia para registrar a próxima compra.

class CaixaRegistradora:
    def __init__(self):
        self.total_compra = 0

    def registrar_compra(self):
        contador = 1
        while True:
            try:
                preco = float(input(f"Produto {contador} : R$ "))
                if preco < 0:
                    raise ValueError
                if preco == 0:
                    break
                self.total_compra += preco
                contador += 1
            except ValueError:
                print("Preço inválido. Digite um valor válido.")

    def receber_pagamento(self):
        valor_pago = float(input("Dinheiro: R$ "))

        troco = valor_pago - self.total_compra
        print("----- Cupom Fiscal -----")
        contador = 1
        for produto in range(1, contador):
            preco_produto = float(input(f"Produto {contador}: R$ "))
            print(f"Produto {contador}: R$ {preco_produto:.2f}")
            contador += 1
            if preco_produto == 0:
                break

        print(f"Total: R${self.total_compra:.2f}")
        print(f"Dinheiro: R${valor_pago:.2f}")
        print(f"Troco: R${troco:.2f}")

    def reiniciar_caixa(self):
        self.total_compra = 0

if __name__ == "__main__":
    print("Lojas Tabajara")
    caixa = CaixaRegistradora()

    while True:
        caixa.registrar_compra()  # Registra a compra
        caixa.receber_pagamento()  # Recebe o pagamento e calcula o troco
        caixa.reiniciar_caixa()  # Reinicia o caixa para a próxima compra
        print("----- Próxima compra -----")
5