#Lista de Exercício 3 - Questão 36
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para gerar a tabuada de um número.

#O programa recebe um número inteiro do usuário, bem como os valores inicial e final para a tabuada.

#Em seguida, gera a tabuada do número informado, considerando os valores inicial e final.

class Tabuada:
    def __init__(self, numero, inicio, fim):
        self.numero = numero
        self.inicio = inicio
        self.fim = fim

    def gerar_tabuada(self):
        tabuada = []

        for i in range(self.inicio, self.fim + 1):
            resultado = self.numero * i
            tabuada.append((i, resultado))

        return tabuada

if __name__ == "__main__":
    try:
        numero = int(input("Montar a tabuada de: "))
        inicio = int(input("Começar por: "))
        fim = int(input("Terminar em: "))

        print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")

        tabuada = Tabuada(numero, inicio, fim)
        resultado_tabuada = tabuada.gerar_tabuada()

        if len(resultado_tabuada) > 0:
            for item in resultado_tabuada:
                print(f"{numero} X {item[0]} = {item[1]}")
        else:
            print("Não foram gerados resultados.")

    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

