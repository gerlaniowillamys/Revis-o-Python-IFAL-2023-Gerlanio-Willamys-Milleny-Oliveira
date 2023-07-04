#Lista de Exercício 5 - Questão 8
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

class ContadorDigitos:
    @staticmethod
    def contar_digitos(numero):
        return len(str(numero))

    def ler_numero(self):
        while True:
            try:
                num = int(input("Insira um número inteiro: "))
                return num
            except ValueError:
                print("Valor inválido. Por favor, insira um número inteiro.")

    def executar(self):
        num = self.ler_numero()
        qtd_digitos = self.contar_digitos(num)
        print(f"O número {num} tem {qtd_digitos} dígito(s).")

contador = ContadorDigitos()
contador.executar()
