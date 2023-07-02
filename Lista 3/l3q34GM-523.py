#Lista de Exercício 3 - Questão 34
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para verificar se um número é primo.

#O programa recebe um número inteiro do usuário e verifica se ele é primo.

#Um número primo é aquele que é divisível apenas por um e por ele mesmo.

class VerificadorPrimo:
    def __init__(self, numero):
        self.numero = numero

    def verificar_primalidade(self):
        if self.numero < 2:
            return False

        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False

        return True

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))

        verificador = VerificadorPrimo(numero)

        if verificador.verificar_primalidade():
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")

    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")
