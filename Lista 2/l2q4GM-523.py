#Lista de Exercício 2 - Questão 4
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
    print("A letra digitada é uma vogal!")
else:
    print("A letra digitada é uma consoante!")