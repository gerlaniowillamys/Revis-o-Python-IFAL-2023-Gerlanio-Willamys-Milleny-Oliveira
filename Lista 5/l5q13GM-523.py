#Lista de Exercício 5 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def desenhar_moldura(linhas=1, colunas=1):
    if linhas < 1 or linhas > 20:
        linhas = max(1, min(linhas, 20))
    if colunas < 1 or colunas > 20:
        colunas = max(1, min(colunas, 20))

    print('+' + '-' * colunas + '+')
    for _ in range(linhas):
        print('|' + ' ' * colunas + '|')
    print('+' + '-' * colunas + '+')

linhas = int(input("Digite o número de linhas (1 a 20): "))
colunas = int(input("Digite o número de colunas (1 a 20): "))

desenhar_moldura(linhas, colunas)
