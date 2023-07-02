#Lista de Exercício 7 - Questão 6
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe TV: Faça um programa que simule um televisor, criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permaneçam dentro de faixas válidas.

class TV:
    def __init__(self):
        self.canal = 1  # Canal inicial
        self.volume = 5  # Nível de volume inicial

    def alterarCanal(self, novo_canal):
        if novo_canal < 1 or novo_canal > 100:
            raise ValueError("O número do canal deve estar entre 1 e 100.")
        self.canal = novo_canal

    def aumentarVolume(self):
        if self.volume < 10:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1

    def informacoesTV(self):
        print("Canal:", self.canal)
        print("Volume:", self.volume)

# Exemplo de uso da classe TV
try:
    televisao = TV()
    televisao.informacoesTV()
    televisao.alterarCanal(7)
    televisao.aumentarVolume()
    televisao.informacoesTV()
    televisao.diminuirVolume()
    televisao.informacoesTV()
except ValueError as error:
    print("Erro:", str(error))
