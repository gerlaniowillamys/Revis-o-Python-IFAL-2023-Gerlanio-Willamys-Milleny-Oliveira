#Lista de Exercício 4 - Questão 12
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Determinar quantos alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos

class Aluno:
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura

def main():
    try:
        alunos = []  # Lista para armazenar os objetos Aluno

        # Entrada dos dados dos alunos
        for i in range(30):
            idade = int(input(f"Informe a idade do aluno {i+1}: "))
            altura = float(input(f"Informe a altura do aluno {i+1}: "))

            aluno = Aluno(idade, altura)
            alunos.append(aluno)

        # Cálculo da média de altura dos alunos
        soma_alturas = sum(aluno.altura for aluno in alunos)
        media_alturas = soma_alturas / len(alunos)

        # Contagem de alunos com mais de 13 anos e altura inferior à média
        contador = 0
        for aluno in alunos:
            if aluno.idade > 13 and aluno.altura < media_alturas:
                contador += 1

        # Exibição do resultado
        print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {contador}")

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar uma idade válida.")

if __name__ == "__main__":
    main()