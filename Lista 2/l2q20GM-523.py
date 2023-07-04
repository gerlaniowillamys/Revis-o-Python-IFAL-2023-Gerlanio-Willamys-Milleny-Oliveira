#Lista de Exercício 2 - Questão 20
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

class CalculadoraMedia:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("Nota inválida. Digite um valor entre 0 e 10.")
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) != 3:
            raise ValueError("É necessário informar exatamente 3 notas.")

        media = sum(self.notas) / len(self.notas)
        return media

    def obter_status_aprovacao(self):
        media = self.calcular_media()

        if media == 10:
            return "Aprovado com Distinção."
        elif media >= 7:
            return "Aprovado."
        else:
            return "Reprovado."


def main():
    try:
        calculadora = CalculadoraMedia()

        for i in range(3):
            nota = float(input("Digite a {}ª nota: ".format(i + 1)))
            calculadora.adicionar_nota(nota)

        status_aprovacao = calculadora.obter_status_aprovacao()
        print(status_aprovacao)
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
