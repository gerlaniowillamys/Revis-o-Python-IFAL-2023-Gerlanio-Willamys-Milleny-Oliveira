#Lista de Exercício 4 - Questão 14
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Classificar a participação de uma pessoa em um crime com base em suas respostas a 5 perguntas.

class Pergunta:
    def __init__(self, texto):
        self.texto = texto

def main():
    try:
        perguntas = [
            Pergunta("Telefonou para a vítima?"),
            Pergunta("Esteve no local do crime?"),
            Pergunta("Mora perto da vítima?"),
            Pergunta("Devia para a vítima?"),
            Pergunta("Já trabalhou com a vítima?")
        ]

        respostas = []  # Lista para armazenar as respostas

        # Perguntas e obtenção das respostas
        for pergunta in perguntas:
            resposta = input(pergunta.texto + " (S/N): ").upper()
            if resposta == "S" or resposta == "N":
                respostas.append(resposta)
            else:
                raise ValueError

        # Contagem de respostas positivas
        count = respostas.count("S")

        # Classificação baseada nas respostas
        if count == 2:
            classificacao = "Suspeita"
        elif 3 <= count <= 4:
            classificacao = "Cúmplice"
        elif count == 5:
            classificacao = "Assassino"
        else:
            classificacao = "Inocente"

        # Exibição da classificação
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Erro: Resposta inválida. Certifique-se de digitar S ou N.")

if __name__ == "__main__":
    main()