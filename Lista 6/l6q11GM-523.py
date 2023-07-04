#Lista de Exercício 6 - Questão 11
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

class JogoDaForca:
    def __init__(self, palavras):
        self.palavras = palavras
        self.palavra = self.escolher_palavra()
        self.letras_corretas = []
        self.letras_erradas = []
        self.tentativas = 6

    def escolher_palavra(self):
        return random.choice(self.palavras)

    def exibir_palavra(self):
        palavra_mostrada = ''.join([letra if letra in self.letras_corretas else '_ ' for letra in self.palavra])
        print(f'A palavra é: {palavra_mostrada}')

    def verificar_vitoria(self):
        return set(self.palavra) == set(self.letras_corretas)

    def verificar_derrota(self):
        return self.tentativas == 0

    def jogar(self):
        while True:
            self.exibir_palavra()

            if self.verificar_vitoria():
                print('Parabéns! Você venceu!')
                break

            if self.verificar_derrota():
                print(f'Você foi enforcado! A palavra era: {self.palavra}')
                break

            try:
                letra = self.obter_letra()
                self.verificar_letra(letra)
            except ValueError as e:
                print("Ocorreu um erro:", str(e))

    def obter_letra(self):
        while True:
            letra = input('Digite uma letra: ').lower()
            if len(letra) != 1:
                raise ValueError('Digite apenas uma letra.')
            if not letra.isalpha():
                raise ValueError('Digite apenas letras.')
            return letra

    def verificar_letra(self, letra):
        if letra in self.letras_corretas or letra in self.letras_erradas:
            print('Você já tentou essa letra. Tente outra.')
        elif letra in self.palavra:
            self.letras_corretas.append(letra)
            print('Acertou!')
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1
            print(f'Você errou pela {7 - self.tentativas}ª vez. Tente de novo!')


def main():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogos']
    jogo = JogoDaForca(palavras)
    jogo.jogar()


if __name__ == '__main__':
    main()
