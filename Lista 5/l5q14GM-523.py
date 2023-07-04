#Lista de Exercício 5 - Questão 14
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
#8  3  4 
#1  5  9
#6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

import itertools

class QuadradoMagico:
    def __init__(self, quadrado):
        self.quadrado = quadrado

    def verificar_quadrado_magico(self):
        for linha in self.quadrado:
            if sum(linha) != 15:
                return False

        for coluna in range(3):
            if sum(self.quadrado[linha][coluna] for linha in range(3)) != 15:
                return False

        if (self.quadrado[0][0] + self.quadrado[1][1] + self.quadrado[2][2] != 15) or (self.quadrado[0][2] + self.quadrado[1][1] + self.quadrado[2][0] != 15):
            return False

        return True

    @staticmethod
    def encontrar_quadrados_magicos():
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        permutacoes = itertools.permutations(numeros)

        for permutacao in permutacoes:
            quadrado = [[permutacao[0], permutacao[1], permutacao[2]],
                        [permutacao[3], permutacao[4], permutacao[5]],
                        [permutacao[6], permutacao[7], permutacao[8]]]

            quadrado_magico = QuadradoMagico(quadrado)
            if quadrado_magico.verificar_quadrado_magico():
                for linha in quadrado:
                    print(' '.join(str(numero) for numero in linha))
                print()


QuadradoMagico.encontrar_quadrados_magicos()
