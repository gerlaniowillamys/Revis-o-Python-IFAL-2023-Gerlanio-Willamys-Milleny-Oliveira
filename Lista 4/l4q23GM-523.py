#Lista de Exercício 4 - Questão 23
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Certifique-se de ter o arquivo "usuarios.txt" no mesmo diretório do programa Python. O programa lê o arquivo "usuarios.txt" e armazena os dados em uma lista de tuplas chamada "usuarios". Em seguida, ele classifica a lista com base no espaço ocupado em ordem decrescente.
#O programa calcula o espaço total ocupado e o espaço médio ocupado pelos usuários. Em seguida, ele gera o relatório formatado no arquivo "relatorio.txt" usando as funções converte_bytes_para_mb e calcula_percentual para realizar as conversões e cálculos necessários.

def converte_bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def calcula_percentual(espaco, espaco_total):
    return (espaco / espaco_total) * 100

def gera_relatorio():
    usuarios = []
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            nome, espaco = linha.split()
            usuarios.append((nome, int(espaco)))

    usuarios.sort(key=lambda x: x[1], reverse=True)
    espaco_total = sum(espaco for _, espaco in usuarios)
    espaco_medio = espaco_total / len(usuarios)

    with open("relatorio.txt", "w") as relatorio:
        relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        relatorio.write("------------------------------------------------------------------------\n")
        relatorio.write("Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n\n")

        for i, (nome, espaco) in enumerate(usuarios, start=1):
            espaco_mb = converte_bytes_para_mb(espaco)
            percentual = calcula_percentual(espaco, espaco_total)
            relatorio.write(f"{i}\t{nome.ljust(15)}\t{espaco_mb:.2f} MB\t\t{percentual:.2f}%\n")

        relatorio.write("\n")
        relatorio.write(f"Espaço total ocupado: {converte_bytes_para_mb(espaco_total):.2f} MB\n")
        relatorio.write(f"Espaço médio ocupado: {converte_bytes_para_mb(espaco_medio):.2f} MB\n")

gera_relatorio()
