#Lista de Exercício 3 - Questão 23
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#classe Primo representa um número inteiro e contém métodos para verificar se é primo, listar os números primos até o valor fornecido e obter o número de divisões feitas para encontrar os primos.
class Primo:
    def __init__(self, numero):
        self.numero = numero

    def eh_primo(self):#O método eh_primo() verifica se o número é primo, percorrendo todos os valores de 2 até a raiz quadrada do número
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False
        return True

    def listar_primos(self):
        primos = []
        divisoes = 0
        for num in range(2, self.numero + 1):
            primo = Primo(num)
            if primo.eh_primo():
                primos.append(num)
                divisoes += primo.get_divisoes()
        return primos, divisoes

    def get_divisoes(self): #O método get_divisoes() retorna o número de divisões necessárias para verificar se um número é primo
        divisoes = 0
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                divisoes += 1
        return divisoes


def main(): #função main(), o programa solicita ao usuário um número inteiro n e, em seguida, instancia um objeto Primo com esse valor
    try:
        n = int(input("Digite um número inteiro: "))
        if n < 1:
            raise ValueError("O número deve ser maior ou igual a 1.") #ValueError caso o usuário digite um número inválido (menor que 1, por exemplo).50
        primo = Primo(n)
        primos, divisoes = primo.listar_primos()
        print("Números primos encontrados:")
        print(primos)
        print("Número de divisões executadas:", divisoes)
    except ValueError as error:
        print("Erro:", error)


if __name__ == "__main__":
    main()
