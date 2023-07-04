#Lista de Exercício 5 - Questão 9
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

class Reversor:
    @staticmethod
    def reverso(numero):
        numero_str = str(numero)
        reverso_str = numero_str[::-1]
        return int(reverso_str)

    def ler_numero(self):
        while True:
            try:
                num = int(input("Insira um número inteiro: "))
                return num
            except ValueError:
                print("Valor inválido. Por favor, insira um número inteiro.")

    def executar(self):
        numero = self.ler_numero()
        reverso_num = self.reverso(numero)
        print(f"O reverso de {numero} é {reverso_num}.")

reversor = Reversor()
reversor.executar()
