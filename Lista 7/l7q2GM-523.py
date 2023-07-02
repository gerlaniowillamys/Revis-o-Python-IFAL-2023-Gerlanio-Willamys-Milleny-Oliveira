#Lista de Exercício 7 - Questão 2 
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Quadrado: Faça um programa que crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        if novo_lado <= 0:
            raise ValueError("O lado do quadrado deve ser um valor positivo.")
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado ** 2

# Exemplo de uso da classe Quadrado
try:
    meu_quadrado = Quadrado(5)
    print("Lado do quadrado:", meu_quadrado.retornarLado())
    print("Área do quadrado:", meu_quadrado.calcularArea())
    meu_quadrado.mudarLado(7)
    print("Novo lado do quadrado:", meu_quadrado.retornarLado())
    print("Nova área do quadrado:", meu_quadrado.calcularArea())
    meu_quadrado.mudarLado(-2)  # Tentando definir um lado negativo
except ValueError as error:
    print("Erro:", str(error))
