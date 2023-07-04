#Lista de Exercício 4 - Questão 16
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Determinar quantos vendedores receberam salários dentro de faixas específicas.

def main():
    try:
        salarios = [470, 380, 550, 670, 720, 800, 920, 1050, 1230, 930]

        faixas = [
            "$200 - $299",
            "$300 - $399",
            "$400 - $499",
            "$500 - $599",
            "$600 - $699",
            "$700 - $799",
            "$800 - $899",
            "$900 - $999",
            "$1000 em diante"
        ]

        contadores = [0] * len(faixas)  # Inicializa os contadores com zeros

        # Contagem dos salários dentro das faixas
        for salario in salarios:
            indice = obter_indice_faixa(salario)
            contadores[indice] += 1

        # Exibição dos resultados
        for i in range(len(faixas)):
            print(f"{faixas[i]}: {contadores[i]}")

    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar um número válido.")

def obter_indice_faixa(salario):
    faixas = [299, 399, 499, 599, 699, 799, 899, 999]
    for i in range(len(faixas)):
        if salario <= faixas[i]:
            return i
    return len(faixas)

if __name__ == "__main__":
    main()
