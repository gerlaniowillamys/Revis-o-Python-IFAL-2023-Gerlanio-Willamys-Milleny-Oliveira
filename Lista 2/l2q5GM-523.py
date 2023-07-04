#Lista de Exercício 2 - Questão 5
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    if media == 10:
        return "Aprovado com distinção"
    elif media > 5:
        return "Aprovado"
    else:
        return "Reprovado"

if __name__ == "__main__":
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = calcular_media(nota1, nota2)
        situacao = verificar_aprovacao(media)

        print(situacao)

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico válido para as notas.")
    except Exception as e:
        print("Ocorreu um erro:", e)
