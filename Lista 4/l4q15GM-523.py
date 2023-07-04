#Lista de Exercício 4 - Questão 15
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Realizar diversas operações com uma lista de notas informadas pelo usuário.

def main():
    try:
        notas = []
        nota = float(input("Informe uma nota (ou -1 para encerrar): "))

        while nota != -1:
            notas.append(nota)
            nota = float(input("Informe uma nota (ou -1 para encerrar): "))

        # Quantidade de valores lidos
        quantidade = len(notas)
        print(f"Quantidade de valores lidos: {quantidade}")

        # Valores informados na ordem em que foram digitados
        print("Valores informados (ordem original):", end=" ")
        for nota in notas:
            print(nota, end=" ")
        print()

        # Valores informados na ordem inversa
        print("Valores informados (ordem inversa):")
        for nota in reversed(notas):
            print(nota)

        # Soma dos valores
        soma = sum(notas)
        print(f"Soma dos valores: {soma}")

        # Média dos valores
        media = soma / quantidade
        print(f"Média dos valores: {media:.2f}")

        # Quantidade de valores acima da média
        acima_media = sum(nota > media for nota in notas)
        print(f"Quantidade de valores acima da média: {acima_media}")

        # Quantidade de valores abaixo de sete
        abaixo_sete = sum(nota < 7 for nota in notas)
        print(f"Quantidade de valores abaixo de sete: {abaixo_sete}")

        # Mensagem de encerramento
        print("Programa encerrado.")

    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar um número válido.")

if __name__ == "__main__":
    main()
