#Lista de Exercício 1 - Questão 4 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            return nota
        except ValueError:
            print("Entrada inválida. Por favor, digite uma nota válida.")

def calcular_media(notas):
    return sum(notas) / len(notas)

if __name__ == "__main__":
    try:
        notas = []
        for i in range(4):
            nota = obter_nota("Digite a nota do {}º bimestre: ".format(i+1))
            notas.append(nota)

        media = calcular_media(notas)

        print("A média das notas é:", media)
    except Exception as e:
        print("Ocorreu um erro:", e)
