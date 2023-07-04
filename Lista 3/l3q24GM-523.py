#Lista de Exercício 3 - Questão 24
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para calcular a média aritmética de N notas.

#O programa solicita ao usuário a quantidade de notas (N) que deseja inserir.

#Em seguida, solicita as N notas ao usuário e calcula a média aritmética.

#Caso o usuário digite uma nota inválida, o programa trata a exceção e solicita uma nova nota.


class NotaInvalidaError(Exception):
    pass

class CalculadoraMedia:
    def __init__(self):
        self.notas = []  # Lista para armazenar as notas

    def solicitar_quantidade_notas(self):
        while True:
            try:
                quantidade = int(input("Digite a quantidade de notas: "))  # Solicita a quantidade de notas ao usuário
                return quantidade
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro válido.")

    def solicitar_notas(self, quantidade):
        for i in range(quantidade):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1}: "))  # Solicita a nota individual ao usuário
                    if nota < 0 or nota > 10:
                        raise NotaInvalidaError  # Lança a exceção NotaInvalidaError se a nota estiver fora do intervalo
                    self.notas.append(nota)  # Adiciona a nota à lista de notas
                    break
                except ValueError:
                    print("Nota inválida. Digite um número válido.")
                except NotaInvalidaError:
                    print("Nota inválida. Digite um valor entre 0 e 10.")

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)  # Calcula a média aritmética das notas

    def exibir_media(self):
        media = self.calcular_media()  # Chama o método calcular_media para obter a média
        print(f"A média das notas é: {media:.2f}")  # Exibe a média formatada com duas casas decimais


if __name__ == "__main__":
    calculadora = CalculadoraMedia()  # Cria uma instância da classe CalculadoraMedia
    quantidade_notas = calculadora.solicitar_quantidade_notas()  # Solicita a quantidade de notas
    calculadora.solicitar_notas(quantidade_notas)  # Solicita as notas individuais
    calculadora.exibir_media()  # Exibe a média final
