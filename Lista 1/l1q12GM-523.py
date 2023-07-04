#Lista de Exercício 1 - Questão 12
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calcular_peso_ideal(altura):
    return (72.7 * altura) - 58

if __name__ == "__main__":
    try:
        altura = float(input("Digite a altura da pessoa em metros: "))
        peso_ideal = calcular_peso_ideal(altura)
        print("O peso ideal para essa altura é:", peso_ideal, "kg")
    except ValueError:
        print("Entrada inválida. Por favor, digite uma altura válida em metros.")
    except Exception as e:
        print("Ocorreu um erro:", e)
