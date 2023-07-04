#Lista de Exercício 7 - Questão 16
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def comer(self, comida):
        self.fome -= comida
        if self.fome < 0:
            self.fome = 0
        self.saude += comida
        if self.saude > 100:
            self.saude = 100
        self.idade += 1

    def brincar(self, tempo):
        self.fome += tempo
        if self.fome > 100:
            self.fome = 100
        self.saude -= tempo
        if self.saude < 0:
            self.saude = 0
        self.idade += tempo

    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}"


# Função para exibir o menu e interagir com o bichinho virtual
def interagir_com_bichinho(bichinho):
    while True:
        print("\nO que você quer fazer?")
        print("1 - Alimentar o bichinho")
        print("2 - Brincar com o bichinho")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            comida = int(input("Quantas unidades de comida você quer dar? "))
            bichinho.comer(comida)
        elif opcao == "2":
            tempo = int(input("Por quanto tempo você quer brincar? "))
            bichinho.brincar(tempo)
        elif opcao == "0":
            break
        elif opcao == "12345":
            print(bichinho)  # Mostrar os valores exatos dos atributos do bichinho
        else:
            print("Opção inválida. Tente novamente.")


# Criar o bichinho virtual
nome_bichinho = input("Digite o nome do seu bichinho virtual: ")
bichinho_virtual = BichinhoVirtual(nome_bichinho)

# Interagir com o bichinho virtual
interagir_com_bichinho(bichinho_virtual)
