#Lista de Exercício 2 - Questão 3
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def obter_genero(letra):
    if letra == "F":
        return "Feminino"
    elif letra == "M":
        return "Masculino"
    else:
        return "Sexo Inválido"

if __name__ == "__main__":
    try:
        letra = input("Digite uma letra: ").upper()

        genero = obter_genero(letra)

        print(f"{letra} - {genero}")

    except Exception as e:
        print("Ocorreu um erro:", e)
