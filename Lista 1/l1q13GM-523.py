#Lista de Exercício 1 - Questão 13
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

def calcular_peso_ideal(altura, sexo):
    if sexo.upper() == "M":
        return (72.7 * altura) - 58
    elif sexo.upper() == "F":
        return (62.1 * altura) - 44.7
    else:
        raise ValueError("Opção de sexo inválida. Por favor, digite M para masculino ou F para feminino.")

if __name__ == "__main__":
    try:
        altura = float(input("Digite a altura da pessoa em metros: "))
        sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")
        peso_ideal = calcular_peso_ideal(altura, sexo)
        if sexo.upper() == "M":
            print("O peso ideal para um homem com essa altura é:", peso_ideal, "kg")
        elif sexo.upper() == "F":
            print("O peso ideal para uma mulher com essa altura é:", peso_ideal, "kg")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Ocorreu um erro:", e)
