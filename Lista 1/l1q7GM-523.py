#Lista de Exercício 1 - Questão 7 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcular_area_quadrado(lado):
    return lado ** 2

def calcular_dobro_area(area):
    return 2 * area

if __name__ == "__main__":
    try:
        lado = float(input("Digite o valor do lado do quadrado: "))
        area = calcular_area_quadrado(lado)
        dobro_area = calcular_dobro_area(area)
        print("A área do quadrado é:", area)
        print("O dobro da área do quadrado é:", dobro_area)
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor válido para o lado do quadrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)
