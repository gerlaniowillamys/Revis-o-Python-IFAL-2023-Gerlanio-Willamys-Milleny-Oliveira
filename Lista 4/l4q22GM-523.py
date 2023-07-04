#Lista de Exercício 4 - Questão 22
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#O programa utiliza um loop while para solicitar as entradas dos números de identificação e tipos de defeitos dos mouses. Quando o número de identificação digitado for zero, o loop é encerrado.
#O programa mantém um dicionário situacoes_contagem para armazenar a contagem de cada tipo de defeito. No final, ele imprime o relatório com a quantidade e o percentual de cada situação.


def relatorio_mouses():
    situacoes = {
        1: "necessita da esfera",
        2: "necessita de limpeza",
        3: "necessita troca do cabo ou conector",
        4: "quebrado ou inutilizado"
    }
    quantidade_mouses = 0
    situacoes_contagem = {i: 0 for i in situacoes}

    while True:
        identificacao = int(input("Digite o número de identificação do mouse (ou 0 para encerrar): "))
        if identificacao == 0:
            break
        situacao = int(input("Digite o tipo de defeito do mouse (1 a 4): "))
        if situacao not in situacoes:
            print("Opção inválida. Digite um número de 1 a 4.")
            continue
        quantidade_mouses += 1
        situacoes_contagem[situacao] += 1

    print("\nRelatório de Levantamento de Mouses:")
    print("Quantidade de mouses:", quantidade_mouses)
    print("\nSituação\t\tQuantidade\tPercentual")
    for situacao, descricao in situacoes.items():
        quantidade = situacoes_contagem[situacao]
        percentual = (quantidade / quantidade_mouses) * 100
        print(f"{situacao}- {descricao}\t\t{quantidade}\t\t{percentual:.2f}%")

relatorio_mouses()