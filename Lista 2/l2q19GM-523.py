#Lista de Exercício 2 - Questão 19
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

class SeparadorNumero:
    def __init__(self, numero):
        self.numero = numero

    def separar_numero(self):
        if self.numero < 0 or self.numero > 999:
            raise ValueError("Número inválido. Digite um número entre 0 e 999.")

        unidade = self.numero % 10
        numero = (self.numero - unidade) / 10
        dezena = numero % 10
        numero = (numero - dezena) / 10
        centena = numero

        dezena = int(dezena)
        centena = int(centena)

        return centena, dezena, unidade


def main():
    try:
        num = int(input("Digite um número: "))

        separador = SeparadorNumero(num)
        centena, dezena, unidade = separador.separar_numero()

        print("{} centena(s), {} dezena(s), {} unidade(s).".format(centena, dezena, unidade))
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
