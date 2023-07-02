#Lista de Exercício 3 - Questão 4
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Simulação do crescimento populacional de dois países

class Pais:
    def __init__(self, populacao, taxa_crescimento):
        # Inicializa o país com sua população e taxa de crescimento anual
        self.populacao = populacao
        self.taxa_crescimento = taxa_crescimento

    def crescer(self):
        # Simula o crescimento populacional do país
        self.populacao += int(self.populacao * self.taxa_crescimento)


class SimuladorPopulacional:
    def __init__(self, pais_a, pais_b):
        # Inicializa o simulador com dois países
        self.pais_a = pais_a
        self.pais_b = pais_b

    def calcular_anos_necessarios(self):
        # Calcula o número de anos necessários para o país A ultrapassar ou igualar a população do país B
        anos = 0

        while self.pais_a.populacao < self.pais_b.populacao:
            self.pais_a.crescer()
            self.pais_b.crescer()
            anos += 1

        return anos


try:
    # Leitura das informações de entrada do usuário
    populacao_a = int(input("Digite a população do país A: "))
    taxa_crescimento_a = float(input("Digite a taxa de crescimento anual do país A (em decimal): "))
    populacao_b = int(input("Digite a população do país B: "))
    taxa_crescimento_b = float(input("Digite a taxa de crescimento anual do país B (em decimal): "))
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números inteiros para as populações e números decimais para as taxas de crescimento.")
    exit()

# Criação dos objetos Pais
pais_a = Pais(populacao_a, taxa_crescimento_a)
pais_b = Pais(populacao_b, taxa_crescimento_b)

# Criação do SimuladorPopulacional
simulador = SimuladorPopulacional(pais_a, pais_b)

# Cálculo do número de anos necessários
anos_necessarios = simulador.calcular_anos_necessarios()

# Exibição dos resultados
print(f"Após {anos_necessarios} anos, a população do país A ultrapassará ou igualará a população do país B.")
print(f"População do país A: {pais_a.populacao}")
print(f"População do país B: {pais_b.populacao}")
