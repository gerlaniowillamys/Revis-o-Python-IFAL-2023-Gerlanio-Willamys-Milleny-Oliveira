#Lista de Exercício 3 - Questão 25
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Programa para verificar a faixa etária média de uma turma.

#O programa solicita a idade de várias pessoas e calcula a média de idade da turma.

#Em seguida, determina se a turma é jovem, adulta ou idosa, com base na faixa etária média.


class IdadeInvalidaError(Exception):
    pass

class VerificadorFaixaEtaria:
    def __init__(self):
        self.idades = []

    def solicitar_idades(self):
        while True:
            try:
                quantidade = int(input("Digite a quantidade de pessoas: "))  # Solicita a quantidade de pessoas
                if quantidade <= 0:
                    raise IdadeInvalidaError
                break
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro válido.")
            except IdadeInvalidaError:
                print("Quantidade inválida. Digite um valor maior que zero.")

        for i in range(quantidade):
            while True:
                try:
                    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))  # Solicita a idade de cada pessoa
                    if idade <= 0:
                        raise IdadeInvalidaError
                    self.idades.append(idade) 
                     # Adiciona a idade à lista de idades
                    break
                except ValueError:
                    print("Idade inválida. Digite um número inteiro válido.")
                except IdadeInvalidaError:
                    print("Idade inválida. Digite um valor maior que zero.")

    def calcular_media_idade(self):
        if len(self.idades) == 0:
            return 0
        return sum(self.idades) / len(self.idades) 
         # Calcula a média de idade da turma

    def verificar_faixa_etaria(self):
        media_idade = self.calcular_media_idade()
        if 0 <= media_idade <= 25:
            return "jovem"
        elif 26 <= media_idade <= 60:
            return "adulta"
        else:
            return "idosa"

    def exibir_resultado(self):
        faixa_etaria = self.verificar_faixa_etaria()
        print(f"A turma é classificada como {faixa_etaria}.")

if __name__ == "__main__":
    verificador = VerificadorFaixaEtaria()
    verificador.solicitar_idades()
    verificador.exibir_resultado()
