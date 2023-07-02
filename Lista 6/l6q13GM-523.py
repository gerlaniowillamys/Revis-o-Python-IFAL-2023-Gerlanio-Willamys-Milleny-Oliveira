#Lista de Exercício 6 - Questão 13
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random

# Lista de palavras
palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogos']

# Escolher uma palavra aleatoriamente
palavra = random.choice(palavras)

# Embaralhar a palavra
palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))

# Variáveis de controle
tentativas = 6

while True:
    # Exibir a palavra embaralhada
    print(f'A palavra embaralhada é: {palavra_embaralhada}')

    # Verificar se o jogador perdeu todas as tentativas
    if tentativas == 0:
        print(f'Você perdeu! A palavra era: {palavra}')
        break

    # Solicitar uma palavra ao jogador
    palpite = input('Digite sua resposta: ')

    # Verificar se a resposta está correta
    if palpite.lower() == palavra:
        print('Parabéns! Você acertou!')
        break
    else:
        tentativas -= 1
        print(f'Resposta incorreta. Você tem {tentativas} tentativas restantes.')
