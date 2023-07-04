#Lista de Exercício 7 - Questão 11
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#O consumo é especificado no construtor e o nível de combustível inicial é 0.
#Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#Forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        consumo_total = distancia / self.consumo
        if consumo_total <= self.combustivel:
            self.combustivel -= consumo_total
            print(f'O carro percorreu {distancia} km.')
        else:
            print('Combustível insuficiente para percorrer essa distância.')

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade


# Exemplo de uso
meuFusca = Carro(15)  # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20)  # abastece com 20 litros de combustível.
meuFusca.andar(100)  # anda 100 quilômetros.
print(f'Combustível restante: {meuFusca.obterGasolina()} litros.')