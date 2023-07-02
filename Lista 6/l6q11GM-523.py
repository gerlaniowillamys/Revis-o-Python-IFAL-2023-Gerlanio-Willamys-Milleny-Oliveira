#Lista de Exercício 6 - Questão 11
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

# Lista de palavras
palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogos']

# Escolher uma palavra aleatoriamente
palavra = random.choice(palavras)

# Variáveis de controle
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    # Exibir palavra com letras corretas adivinhadas
    palavra_mostrada = ''.join([letra if letra in letras_corretas else '_ ' for letra in palavra])
    print(f'A palavra é: {palavra_mostrada}')

    # Verificar se a palavra foi completamente adivinhada
    if set(palavra) == set(letras_corretas):
        print('Parabéns! Você venceu!')
        break

    # Verificar se o jogador perdeu todas as tentativas
    if tentativas == 0:
        print(f'Você foi enforcado! A palavra era: {palavra}')
        break

    # Solicitar uma letra ao jogador
    letra = input('Digite uma letra: ').lower()

    # Verificar se a letra já foi digitada
    if letra in letras_corretas or letra in letras_erradas:
        print('Você já tentou essa letra. Tente outra.')
        continue

    # Verificar se a letra está na palavra
    if letra in palavra:
        letras_corretas.append(letra)
        print('Acertou!')
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print(f'Você errou pela {7 - tentativas}ª vez. Tente de novo!')