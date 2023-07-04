#Lista de Exercício 4 - Questão 19
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


	#recebe o número de votos para uma opção e o total de votos, e calcula o percentual correspondente.
def calcular_percentual(votos, total_votos):
    percentual = (votos / total_votos) * 100
    return percentual


def main(): #função main, é criada uma lista votos com 7 elementos, onde cada elemento representa a quantidade de votos para uma opção
    votos = [0] * 7
    total_votos = 0
    opcoes = ["", "Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"] #Também é criada uma lista opcoes que armazena as opções válidas para a enquete.

    print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?\n")
    print("Opções:")
    print("1- Windows Server")
    print("2- Unix")
    print("3- Linux")
    print("4- Netware")
    print("5- Mac OS")
    print("6- Outro")
    print("0- Encerrar votação\n")

    while True:
        try:
            voto = int(input("Informe o número da opção desejada: "))
        except ValueError:
            print("Informe um valor válido.\n")
            continue

        if voto == 0:
            break

        if voto < 0 or voto > 6:
            print("Opção inválida. Informe um valor entre 0 e 6.\n")
            continue

        votos[voto] += 1
        total_votos += 1

    print("\nResultado da votação:\n")
    print("Sistema Operacional     Votos      %")
    print("-------------------     -----     ---")

    for i in range(1, 7):
        percentual = calcular_percentual(votos[i], total_votos)
        print(f"{opcoes[i]:<23}   {votos[i]:<7}{percentual:>3.0f}%")

    print("-------------------     -----     ---")
    print(f"Total                     {total_votos}\n")

    vencedor = votos.index(max(votos[1:])) #função max(votos[1:]) é utilizada para encontrar o vencedor, excluindo a opção de índice 0.
    percentual_vencedor = calcular_percentual(votos[vencedor], total_votos)
    print(f"O Sistema Operacional mais votado foi o {opcoes[vencedor]}, com {votos[vencedor]} votos, correspondendo a {percentual_vencedor:.0f}% dos votos.")


if __name__ == "__main__":
    main()
