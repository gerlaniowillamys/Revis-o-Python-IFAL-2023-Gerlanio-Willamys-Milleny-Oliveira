#Lista de Exercício 3 - Questão 45
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenado

def calcular_media_saltos(nome):
    saltos = []

    for i in range(1, 6):
        distancia = float(input(f"{i}º Salto: "))
        saltos.append(distancia)

    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)
    media_saltos = sum(saltos) / len(saltos)

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {media_saltos} m")


# Exemplo de uso
while True:
    nome_atleta = input("Digite o nome do atleta (ou deixe em branco para sair): ")
    if nome_atleta == "":
        break

    print("\n")
    calcular_media_saltos(nome_atleta)
    print("\n")
