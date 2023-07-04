#Lista de Exercício 2 - Questão 4
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def verificar_vogal_consoante(letra):
    if letra in 'aeiou':
        return "vogal"
    else:
        return "consoante"

if __name__ == "__main__":
    try:
        letra = input("Digite uma letra: ").lower()

        tipo_letra = verificar_vogal_consoante(letra)

        print("A letra digitada é uma", tipo_letra)

    except Exception as e:
        print("Ocorreu um erro:", e)
