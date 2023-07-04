#Lista de Exercício 3 - Questão 5
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Simulação do crescimento populacional de dois países

class Pais:
    def __init__(self, populacao, taxa_crescimento):
        self.populacao = populacao
        self.taxa_crescimento = taxa_crescimento

    def crescer(self):
        self.populacao += int(self.populacao * self.taxa_crescimento)


class SimuladorPopulacional:
    def __init__(self, pais_a, pais_b):
        self.pais_a = pais_a
        self.pais_b = pais_b

    def calcular_anos_necessarios(self):
        anos = 0

        while self.pais_a.populacao < self.pais_b.populacao:
            self.pais_a.crescer()
            self.pais_b.crescer()
            anos += 1

        return anos


while True:
    try:
        populacao_a = int(input("Digite a população do país A: "))
        taxa_crescimento_a = float(input("Digite a taxa de crescimento anual do país A (em decimal): "))
        populacao_b = int(input("Digite a população do país B: "))
        taxa_crescimento_b = float(input("Digite a taxa de crescimento anual do país B (em decimal): "))
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números inteiros para as populações e números decimais para as taxas de crescimento.")
        continue

    pais_a = Pais(populacao_a, taxa_crescimento_a)
    pais_b = Pais(populacao_b, taxa_crescimento_b)

    simulador = SimuladorPopulacional(pais_a, pais_b)
    anos_necessarios = simulador.calcular_anos_necessarios()

    print(f"Após {anos_necessarios} anos, a população do país A ultrapassará ou igualará a população do país B.")
    print(f"População do país A: {pais_a.populacao}")
    print(f"População do país B: {pais_b.populacao}")

    opcao = input("Deseja realizar outra simulação? (S/N): ")
    if opcao.upper() != 'S':
        break
