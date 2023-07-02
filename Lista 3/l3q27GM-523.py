#Lista de Exercício 3 - Questão 27
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Programa para calcular o número médio de alunos por turma.

#O programa solicita a quantidade de turmas e a quantidade de alunos em cada turma.
#Em seguida, calcula o número médio de alunos por turma.



class AlunosExcedidosError(Exception):
    pass

class CalculadoraMediaAlunos:
    def __init__(self):
        self.num_turmas = 0
        self.total_alunos = 0

    def solicitar_quantidade_turmas(self):
        while True:
            try:
                self.num_turmas = int(input("Digite a quantidade de turmas: "))  # Solicita a quantidade de turmas
                if self.num_turmas <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro maior que zero.")

    def solicitar_quantidade_alunos(self):
        for i in range(self.num_turmas):
            while True:
                try:
                    quantidade = int(input(f"Digite a quantidade de alunos na turma {i + 1}: "))  # Solicita a quantidade de alunos na turma
                    if quantidade <= 0 or quantidade > 40:
                        raise AlunosExcedidosError
                    self.total_alunos += quantidade  
                    # Adiciona a quantidade de alunos ao total
                    break
                except ValueError:
                    print("Quantidade inválida. Digite um número inteiro válido.")
                except AlunosExcedidosError:
                    print("Quantidade inválida. Digite um valor entre 1 e 40.")

    def calcular_media_alunos(self):
        if self.num_turmas == 0:
            return 0
        return self.total_alunos / self.num_turmas  
        # Calcula o número médio de alunos por turma

    def exibir_resultado(self):
        media_alunos = self.calcular_media_alunos()
        print(f"O número médio de alunos por turma é: {media_alunos:.2f}")

if __name__ == "__main__":
    calculadora = CalculadoraMediaAlunos()
    calculadora.solicitar_quantidade_turmas()  
    # Solicita a quantidade de turmas
    calculadora.solicitar_quantidade_alunos()  
    # Solicita a quantidade de alunos em cada turma
    calculadora.exibir_resultado()  # Exibe o resultado da média de alunos por turma

