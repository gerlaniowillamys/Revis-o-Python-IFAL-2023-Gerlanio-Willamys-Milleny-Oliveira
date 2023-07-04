#Lista de Exercício 4 - Questão 17
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#competição de salto a distância

class Atleta:#classe Atleta é definida com os atributos nome e saltos
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []
				#método adicionar_salto permite adicionar uma distância aos saltos do atleta
    def adicionar_salto(self, distancia):
        self.saltos.append(distancia)
					#método calcular_media_saltos calcula a média das distâncias alcançadas nos saltos.
    def calcular_media_saltos(self):
        return sum(self.saltos) / len(self.saltos)


def main(): #função main, é criada uma lista vazia atletas para armazenar todos os atletas
    atletas = []

    while True: #O loop while solicita o nome do atleta e, se nenhum nome for fornecido, o loop é interrompido
        nome = input("Atleta (ou deixe em branco para sair): ")
        if not nome:
            break

        atleta = Atleta(nome)

        for i in range(1, 6): #um loop for solicita a distância de cada salto e os adiciona ao objeto Atleta usando o método adicionar_salto
            salto = float(input(f"Digite a distância do {i}º salto (em metros): "))
            atleta.adicionar_salto(salto)

        atletas.append(atleta)

    for atleta in atletas:
        print("\nResultado final:")
        print(f"Atleta: {atleta.nome}")
        print(f"Saltos: {' - '.join(str(salto) for salto in atleta.saltos)}")
        print(f"Média dos saltos: {atleta.calcular_media_saltos()} m")


if __name__ == "__main__":
    main()
