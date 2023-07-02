#Lista de Exercício 3 - Questão 1 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para solicitar uma nota entre zero e dez ao usuário

# Definição da classe de exceção personalizada para notas inválidas
class NotaInvalidaError(Exception):
    pass


# Classe responsável por solicitar a nota ao usuário
class SolicitadorNota:
    def solicitar_nota(self):
        while True:
            try:
                # Solicitar a nota ao usuário
                nota = float(input("Digite uma nota entre zero e dez: "))

                # Verificar se a nota está dentro do intervalo válido
                if nota >= 0 and nota <= 10:
                    return nota
                else:
                    raise NotaInvalidaError

            except ValueError:
                # Tratar erro de entrada inválida
                print("Entrada inválida. Digite um valor numérico.")

            except NotaInvalidaError:
                # Tratar erro de valor de nota inválido
                print("Valor inválido. Tente novamente.")


# Instanciar o objeto SolicitadorNota
solicitador = SolicitadorNota()

# Chamar o método para solicitar a nota
nota_digitada = solicitador.solicitar_nota()

# Exibir a nota digitada
print("A nota digitada foi:", nota_digitada)
