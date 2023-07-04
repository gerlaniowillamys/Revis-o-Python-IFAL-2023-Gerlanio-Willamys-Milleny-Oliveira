#Lista de Exercício 3 - Questão 47
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#programa para competição de ginástica

#usada para representar um ginasta e suas notas.
class Ginasta:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        
#usado para adicionar uma nota à lista de notas do ginasta
    def adicionar_nota(self, nota):
        self.notas.append(nota)
        
#remove a maior e a menor nota da lista e calcula a média das notas restantes
    def calcular_media(self):
        # Exclui a maior e a menor nota
        notas_ordenadas = sorted(self.notas)
        notas_ordenadas = notas_ordenadas[1:-1]
        
        # Calcula a média das notas restantes
        media = sum(notas_ordenadas) / len(notas_ordenadas)
        return round(media, 2)
        
#imprime o nome do ginasta, a melhor nota, a pior nota e a média.
    def exibir_resultado(self):
        print("Resultado final:")
        print("Atleta:", self.nome)
        print("Melhor nota:", max(self.notas))
        print("Pior nota:", min(self.notas))
        print("Média:", self.calcular_media())

#Na função main, solicitamos o nome do ginasta e, em seguida, pedimos ao usuário para inserir as notas dos sete jurados
def main():
    nome_ginasta = input("Atleta: ")
    ginasta = Ginasta(nome_ginasta)

    for i in range(7):
        nota = float(input("Nota: "))
        ginasta.adicionar_nota(nota)
        
#mostra o resultado final com base nas notas inseridas.
    ginasta.exibir_resultado()


if __name__ == "__main__":
    main()
