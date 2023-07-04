#Lista de Exercício 3 - Questão 43
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#cardapio de uma lanchonete 
#programa para atender os pedidos dos clientes

#A classe Pedido é criada para representar o pedido do cliente
class Pedido:
    def __init__(self):
        self.cardapio = {
            '100': {'especificacao': 'Cachorro Quente', 'preco': 1.20},
            '101': {'especificacao': 'Bauru Simples', 'preco': 1.30},
            '102': {'especificacao': 'Bauru com ovo', 'preco': 1.50},
            '103': {'especificacao': 'Hambúrguer', 'preco': 1.20},
            '104': {'especificacao': 'Cheeseburguer', 'preco': 1.30},
            '105': {'especificacao': 'Refrigerante', 'preco': 1.00}
        }
        self.total_pedido = 0
    #O método adicionar_item recebe o código do item e a quantidade desejada
    def adicionar_item(self, codigo, quantidade):
        if codigo in self.cardapio:
            item = self.cardapio[codigo]
            valor_item = item['preco'] * quantidade
            self.total_pedido += valor_item
            print(f"{item['especificacao']} - R$ {item['preco']:.2f} x {quantidade} = R$ {valor_item:.2f}")
        else:
            print("Código do item inválido. Tente novamente.")
    #O método calcular_valor_pedido é responsável por solicitar ao usuário os códigos e quantidades dos itens e realizar o cálculo do valor total do pedido
    def calcular_valor_pedido(self):
        print("Cardápio da Lanchonete")
        
        print("Especificação   Código  Preço")
        for codigo, item in self.cardapio.items():
            print(f"{item['especificacao']}{' '*(15-len(item['especificacao']))}  {codigo}{' '*(6-len(codigo))} R$ {item['preco']:.2f}")
        
        while True:
            try:
                codigo = input("Digite o código do item (ou '0' para encerrar o pedido): ")
                
                if codigo == '0':
                    break
                
                quantidade = int(input("Digite a quantidade desejada: "))
                self.adicionar_item(codigo, quantidade)
            
            except ValueError:
                print("Erro: valor inválido digitado.")
                continue
        
        print(f"Total geral do pedido: R$ {self.total_pedido:.2f}")


pedido = Pedido()
pedido.calcular_valor_pedido()
