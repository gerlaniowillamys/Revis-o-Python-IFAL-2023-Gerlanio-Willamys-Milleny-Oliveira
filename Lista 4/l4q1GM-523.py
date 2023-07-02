#Lista de Exercício 4 - Questão 1 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Programa que lê um vetor de 5 números inteiros e os exibe.

class VetorNumeros:
    def __init__(self):
        self.vetor = []

    def ler_vetor(self):
        for i in range(5):
            try:
                num = int(input("Digite um número inteiro: "))
                self.vetor.append(num)
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
                i -= 1  # Tenta novamente para o mesmo índice

    def mostrar_vetor(self):
        print("Números do vetor:")
        for num in self.vetor:
            print(num)

# Criando uma instância da classe VetorNumeros
vetor_nums = VetorNumeros()

# Chamando os métodos para ler e mostrar o vetor
vetor_nums.ler_vetor()
vetor_nums.mostrar_vetor()
