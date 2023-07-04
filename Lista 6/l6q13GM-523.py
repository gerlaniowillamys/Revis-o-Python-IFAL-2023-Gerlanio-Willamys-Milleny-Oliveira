#Lista de Exercício 6 - Questão 13
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random

class JogoAdivinhacaoPalavras:
    def __init__(self):
        self.palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogos']
        self.tentativas = 6
        self.palavra = ''
        self.palavra_embaralhada = ''

    def escolher_palavra(self):
        self.palavra = random.choice(self.palavras)
        self.palavra_embaralhada = ''.join(random.sample(self.palavra, len(self.palavra)))

    def exibir_palavra_embaralhada(self):
        print(f'A palavra embaralhada é: {self.palavra_embaralhada}')

    def solicitar_palpite(self):
        palpite = input('Digite sua resposta: ')
        return palpite.lower()

    def verificar_palpite(self, palpite):
        if palpite == self.palavra:
            print('Parabéns! Você acertou!')
            return True
        else:
            self.tentativas -= 1
            print(f'Resposta incorreta. Você tem {self.tentativas} tentativas restantes.')
            return False

    def jogar(self):
        print('Jogo de Adivinhação de Palavras')
        self.escolher_palavra()

        while True:
            self.exibir_palavra_embaralhada()

            if self.tentativas == 0:
                print(f'Você perdeu! A palavra era: {self.palavra}')
                break

            palpite = self.solicitar_palpite()

            if self.verificar_palpite(palpite):
                break

if __name__ == '__main__':
    jogo = JogoAdivinhacaoPalavras()
    jogo.jogar()
