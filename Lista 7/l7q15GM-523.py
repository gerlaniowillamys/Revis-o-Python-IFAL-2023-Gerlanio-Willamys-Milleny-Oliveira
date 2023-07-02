#Lista de Exercício 7 - Questão 15
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Bichinho Virtual++ - Tamagushi

class Tamagushi:
    def __init__(self, nome, fome, saude, idade, tedio):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def alterar_tedio(self, novo_tedio):
        self.tedio = novo_tedio

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_tedio(self):
        return self.tedio

    def calcular_humor(self):
        humor = self.fome + self.saude
        return humor

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira


# Testando a classe

# Criando um objeto Tamagushi
meu_tamagushi = Tamagushi("noah", 8, 9, 2, 10)

# Obtendo informações do Tamagushi
print("Nome:", meu_tamagushi.retornar_nome())
print("Fome:", meu_tamagushi.retornar_fome())
print("Saúde:", meu_tamagushi.retornar_saude())
print("Idade:", meu_tamagushi.retornar_idade())
print("Tédio:", meu_tamagushi.retornar_tedio())

# Interagindo com o Tamagushi
quantidade_comida = int(input("Quanta comida você quer fornecer? "))
tempo_brincadeira = int(input("Quanto tempo você quer brincar com o Tamagushi? "))

# Alimentando o Tamagushi
meu_tamagushi.alimentar(quantidade_comida)

# Brincando com o Tamagushi
meu_tamagushi.brincar(tempo_brincadeira)

# Obtendo as novas informações do Tamagushi
print("Nome:", meu_tamagushi.retornar_nome())
print("Fome:", meu_tamagushi.retornar_fome())
print("Saúde:", meu_tamagushi.retornar_saude())
print("Idade:", meu_tamagushi.retornar_idade())
print("Tédio:", meu_tamagushi.retornar_tedio())

# Calculando o humor do Tamagushi
humor = meu_tamagushi.calcular_humor()
print("Humor:", humor)
