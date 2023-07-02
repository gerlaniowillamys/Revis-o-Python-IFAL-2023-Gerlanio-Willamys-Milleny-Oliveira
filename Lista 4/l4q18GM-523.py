#Lista de Exercício 4 - Questão 18
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

	#função calcular_percentual recebe o número de votos de um jogador e o total de votos e calcula o percentual correspondente.
def calcular_percentual(votos_jogador, total_votos):
    percentual = (votos_jogador / total_votos) * 100
    return percentual

#função gravar_resultados é responsável por gravar os resultados da votação em um arquivo de texto chamado "resultado_enquete.txt"
def gravar_resultados(resultado):
    with open("resultado_enquete.txt", "w") as arquivo:
        arquivo.write("Resultado da votação:\n\n")
        arquivo.write("Jogador    Votos    %\n")
        arquivo.write("-----------------------\n")
        for jogador, votos, percentual in resultado:
            arquivo.write(f"{jogador:<10}{votos:<9}{percentual:>5.1f}%\n")


def main(): #função main, é criada uma lista votos_jogadores com 24 elementos. Cada elemento da lista representa a quantidade de votos para um determinado jogador, identificado pelo seu número.
    votos_jogadores = [0] * 24  # Índice 0 não será utilizado
    total_votos = 0

    print("Enquete: Quem foi o melhor jogador?\n")

    while True:
        try:
            numero_jogador = int(input("Número do jogador (0=fim): "))
        except ValueError:
            print("Informe um valor válido.\n")
            continue

        if numero_jogador == 0:
            break

        if numero_jogador < 1 or numero_jogador > 23:
            print("Informe um valor entre 1 e 23 ou 0 para sair!\n")
            continue

        votos_jogadores[numero_jogador] += 1
        total_votos += 1

    resultado = []
    melhor_jogador = 0
    maior_votos = 0

    print("\nResultado da votação:\n")
    print("Jogador    Votos    %")
 

    for jogador, votos in enumerate(votos_jogadores):
        if votos > 0:
            percentual = calcular_percentual(votos, total_votos)
            resultado.append((jogador, votos, percentual))

            print(f"{jogador:<10}{votos:<9}{percentual:>5.1f}%")

            if votos > maior_votos:
                melhor_jogador = jogador
                maior_votos = votos

    print(f"\nO melhor jogador foi o número {melhor_jogador}, com {maior_votos} votos, correspondendo a {calcular_percentual(maior_votos, total_votos):.1f}% do total de votos.")

    gravar_resultados(resultado)


if __name__ == "__main__":
    main()
