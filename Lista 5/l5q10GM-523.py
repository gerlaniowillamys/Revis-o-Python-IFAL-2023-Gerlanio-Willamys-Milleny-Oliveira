#Lista de Exercício 5 - Questão 10
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

class CrapsGame:
    def __init__(self):
        self.point = 0

    @staticmethod
    def roll_dice():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1 + dice2

    def play(self):
        while True:
            input("Pressione ENTER para lançar os dados...")
            roll = self.roll_dice()
            print("Você lançou um", roll)

            if self.point == 0:
                if roll == 7 or roll == 11:
                    print("Natural! Você ganhou!")
                    break
                elif roll == 2 or roll == 3 or roll == 12:
                    print("Craps! Você perdeu!")
                    break
                else:
                    self.point = roll
                    print("Seu ponto é", self.point)
            else:
                if roll == self.point:
                    print("Você tirou seu ponto! Você ganhou!")
                    break
                elif roll == 7:
                    print("Você tirou um 7! Você perdeu!")
                    break

game = CrapsGame()
game.play()
