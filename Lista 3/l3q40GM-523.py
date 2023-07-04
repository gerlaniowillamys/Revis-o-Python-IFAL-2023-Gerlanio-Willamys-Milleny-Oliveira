#Lista de Exercício 3 - Questão 40
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

class Cidade:
    def __init__(self, codigo, veiculos, acidentes):
        self.codigo = codigo
        self.veiculos = veiculos
        self.acidentes = acidentes

    def indice_acidentes(self):
        return self.acidentes / self.veiculos


def main():
    # Lista para armazenar as cidades
    cidades = []

    try:
        # Coleta dos dados das cinco cidades
        for i in range(5):
            codigo = int(input(f"Informe o código da cidade {i+1}: "))
            veiculos = int(input("Informe o número de veículos de passeio (em 1999): "))
            acidentes = int(input("Informe o número de acidentes de trânsito com vítimas (em 1999): "))

            # Criação do objeto Cidade e adição à lista
            cidade = Cidade(codigo, veiculos, acidentes)
            cidades.append(cidade)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir apenas números.")

    # Verificação do maior e menor índice de acidentes
    maior_indice = 0
    menor_indice = float("inf")
    cidade_maior_indice = None
    cidade_menor_indice = None

    for cidade in cidades:
        indice = cidade.indice_acidentes()

        if indice > maior_indice:
            maior_indice = indice
            cidade_maior_indice = cidade.codigo

        if indice < menor_indice:
            menor_indice = indice
            cidade_menor_indice = cidade.codigo

    # Cálculo da média de veículos nas cinco cidades
    soma_veiculos = sum(cidade.veiculos for cidade in cidades)
    media_veiculos = soma_veiculos / len(cidades)

    # Cálculo da média de acidentes nas cidades com menos de 2.000 veículos
    cidades_menos_2000 = [cidade for cidade in cidades if cidade.veiculos < 2000]

    if cidades_menos_2000:
        soma_acidentes = sum(cidade.acidentes for cidade in cidades_menos_2000)
        media_acidentes = soma_acidentes / len(cidades_menos_2000)
    else:
        media_acidentes = 0

    # Exibição dos resultados
    print(f"O maior índice de acidentes de trânsito é {maior_indice} e pertence à cidade {cidade_maior_indice}.")
    print(f"O menor índice de acidentes de trânsito é {menor_indice} e pertence à cidade {cidade_menor_indice}.")
    print(f"A média de veículos nas cinco cidades é {media_veiculos:.2f}.")
    print(f"A média de acidentes de trânsito nas cidades com menos de 2.000 veículos é {media_acidentes:.2f}.")


if __name__ == '__main__':
    main()
