#Lista de Exercício 7 - Questão 6
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe TV: Faça um programa que simule um televisor, criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permaneçam dentro de faixas válidas.

class TV:
    def __init__(self):
        self._canal = 1  # Canal inicial
        self._volume = 5  # Nível de volume inicial

    def alterarCanal(self, novo_canal):
        if novo_canal < 1 or novo_canal > 100:
            raise ValueError("O número do canal deve estar entre 1 e 100.")
        self._canal = novo_canal

    def aumentarVolume(self):
        if self._volume < 10:
            self._volume += 1

    def diminuirVolume(self):
        if self._volume > 0:
            self._volume -= 1

    def mostrarInformacoes(self):
        return "Canal: {}, Volume: {}".format(self._canal, self._volume)

# Exemplo de uso da classe TV
try:
    televisao = TV()
    print(televisao.mostrarInformacoes())
    televisao.alterarCanal(7)
    televisao.aumentarVolume()
    print(televisao.mostrarInformacoes())
    televisao.diminuirVolume()
    print(televisao.mostrarInformacoes())
except ValueError as error:
    print("Erro:", str(error))
