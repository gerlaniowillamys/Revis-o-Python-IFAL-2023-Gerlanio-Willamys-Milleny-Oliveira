#Lista de Exercício 4 - Questão 4
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler um vetor de 10 caracteres, contar as consoantes e imprimir as consoantes.

class ContadorConsoantes:
    def __init__(self):
        self.vetor = []  # Lista vazia para armazenar os caracteres

    def ler_vetor(self):
        # Função para ler os caracteres e armazená-los no vetor
        try:
            for i in range(10):
                caractere = input(f"Digite o caractere {i+1}: ")
                self.vetor.append(caractere)
        except:
            print("Erro ao ler o caractere.")

    def contar_consoantes(self):
        # Função para contar as consoantes e imprimir as consoantes
        consoantes = []
        for caractere in self.vetor:
            if self.eh_consoante(caractere):
                consoantes.append(caractere)

        print("Consoantes encontradas:")
        for consoante in consoantes:
            print(consoante)

        print("Total de consoantes:", len(consoantes))

    def eh_consoante(self, caractere):
        # Função para verificar se o caractere é uma consoante
        consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return caractere in consoantes

# Cria um objeto da classe ContadorConsoantes
contador = ContadorConsoantes()

# Chama a função ler_vetor para ler os caracteres
contador.ler_vetor()

# Chama a função contar_consoantes para contar e imprimir as consoantes
contador.contar_consoantes()

