#Lista de Exercício 3 - Questão 26
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Programa para registrar votos em uma eleição com três candidatos.

#O programa solicita o número total de eleitores.

#Em seguida, solicita que cada eleitor vote em um candidato (1, 2 ou 3).

#Ao final, mostra o número de votos de cada candidato.

class VotoInvalidoError(Exception):
    pass

class Eleicao:
    def __init__(self):
        self.total_eleitores = 0
        self.votos = [0, 0, 0]  # Inicializa a contagem de votos para cada candidato

    def solicitar_numero_eleitores(self):
        while True:
            try:
                self.total_eleitores = int(input("Digite o número total de eleitores: "))  # Solicita o número total de eleitores
                if self.total_eleitores <= 0:
                    raise VotoInvalidoError
                break
            except ValueError:
                print("Número inválido. Digite um valor inteiro válido.")
            except VotoInvalidoError:
                print("Número inválido. Digite um valor maior que zero.")

    def registrar_votos(self):
        for i in range(self.total_eleitores):
            while True:
                try:
                    voto = int(input(f"Eleitor {i + 1}, vote em um candidato (1, 2 ou 3): "))  # Solicita o voto de cada eleitor
                    if voto < 1 or voto > 3:
                        raise VotoInvalidoError
                    self.votos[voto - 1] += 1  # Incrementa o número de votos do candidato correspondente
                    break
                except ValueError:
                    print("Voto inválido. Digite um número inteiro válido.")
                except VotoInvalidoError:
                    print("Voto inválido. Digite 1, 2 ou 3 para votar em um candidato.")

    def exibir_resultado(self):
        print("Resultado da eleição:")
        for i, votos_candidato in enumerate(self.votos, start=1):
            print(f"Candidato {i}: {votos_candidato} votos")

if __name__ == "__main__":
    eleicao = Eleicao()
    eleicao.solicitar_numero_eleitores()  
    # Solicita o número total de eleitores
    eleicao.registrar_votos()  # Registra os votos dos eleitores
    eleicao.exibir_resultado()  # Exibe o resultado da eleição
