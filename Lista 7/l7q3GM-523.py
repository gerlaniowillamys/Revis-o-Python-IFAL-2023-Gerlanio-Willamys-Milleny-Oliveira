#Lista de Exercício 7 - Questão 3
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Retangulo: Faça um programa que crie uma classe que modele um retângulo:
# A. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# B. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro
# C. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
#    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        if novo_lado_a <= 0 or novo_lado_b <= 0:
            raise ValueError("Os lados do retângulo devem ser valores positivos.")
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

# Função auxiliar para calcular a quantidade de pisos e rodapés necessários
def calcularPisosERodapes(area):
    area_piso = 1  # Área de cada piso em metros quadrados
    comprimento_rodape = 0.1  # Comprimento de cada rodapé em metros

    quantidade_pisos = area // area_piso
    quantidade_rodapes = (2 * (area_piso + comprimento_rodape)) / comprimento_rodape

    return quantidade_pisos, quantidade_rodapes

# Programa principal
try:
    # Solicita as medidas do local ao usuário
    comprimento = float(input("Digite o comprimento do local em metros: "))
    largura = float(input("Digite a largura do local em metros: "))

    # Cria um objeto Retangulo com as medidas informadas
    local = Retangulo(comprimento, largura)

    # Calcula a área e o perímetro do local
    area_local = local.calcularArea()
    perimetro_local = local.calcularPerimetro()

    # Calcula a quantidade de pisos e rodapés necessários
    quantidade_pisos, quantidade_rodapes = calcularPisosERodapes(area_local)

    # Exibe os resultados
    print("\nÁrea do local:", area_local, "metros quadrados")
    print("Perímetro do local:", perimetro_local, "metros")
    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)
except ValueError as error:
    print("Erro:", str(error))
