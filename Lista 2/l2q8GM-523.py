#Lista de Exercício 2 - Questão 8
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def encontrar_produto_mais_barato(prod1, prod2, prod3):
    if prod1 < prod2 and prod1 < prod3:
        return "O primeiro produto é o mais barato."
    elif prod2 < prod1 and prod2 < prod3:
        return "O segundo produto é o mais barato."
    elif prod3 < prod1 and prod3 < prod2:
        return "O terceiro produto é o mais barato."
    else:
        return "Os produtos têm o mesmo preço."

def main():
    try:
        prod1 = float(input("Digite o valor do primeiro produto: "))
        prod2 = float(input("Digite o valor do segundo produto: "))
        prod3 = float(input("Digite o valor do terceiro produto: "))

        resultado = encontrar_produto_mais_barato(prod1, prod2, prod3)
        print(resultado)

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico válido para os produtos.")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()
