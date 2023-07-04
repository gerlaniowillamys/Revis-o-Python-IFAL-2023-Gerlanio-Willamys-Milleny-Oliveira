#Lista de Exercício 1 - Questão 5 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que converta metros para centímetros.

def converter_para_centimetros(metros):
    return metros * 100

if __name__ == "__main__":
    try:
        metros = float(input("Digite a medida em metros: "))
        centimetros = converter_para_centimetros(metros)
        print("A medida em centímetros é:", centimetros, "cm")
    except ValueError:
        print("Entrada inválida. Por favor, digite uma medida válida.")
    except Exception as e:
        print("Ocorreu um erro:", e)
