#Lista de Exercício 7 - Questão 1 
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Bola: Faça um programa que crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        if nova_cor == self.cor:
            raise ValueError("A cor nova é igual à cor atual.")
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

    def calculaVolume(self):
        raise NotImplementedError("Método 'calculaVolume' não implementado.")

# Exemplo de uso da classe Bola
try:
    minha_bola = Bola("azul", 10, "couro")
    print("Cor atual da bola:", minha_bola.mostraCor())
    minha_bola.trocaCor("vermelho")
    print("Nova cor da bola:", minha_bola.mostraCor())
    minha_bola.trocaCor("vermelho")  # Tentando trocar para a mesma cor novamente
except ValueError as error:
    print("Erro:", str(error))
except NotImplementedError as error:
    print("Erro:", str(error))
