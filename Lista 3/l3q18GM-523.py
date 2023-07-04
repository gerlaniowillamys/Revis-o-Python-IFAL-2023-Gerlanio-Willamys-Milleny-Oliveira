#Lista de Exercício 3 - Questão 18
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para determinar o menor valor, o maior valor e a soma dos valores de um conjunto de números

class AnalisadorConjuntoNumeros:
    def __init__(self):
        self.valores = []

    def adicionar_valor(self, valor):
        self.valores.append(valor)

    def obter_menor_valor(self):
        if not self.valores:
            raise ValueError("Não há valores para analisar.")

        menor_valor = min(self.valores)
        return menor_valor

    def obter_maior_valor(self):
        if not self.valores:
            raise ValueError("Não há valores para analisar.")

        maior_valor = max(self.valores)
        return maior_valor

    def obter_soma_valores(self):
        if not self.valores:
            raise ValueError("Não há valores para analisar.")

        soma_valores = sum(self.valores)
        return soma_valores

def main():
    print("Analisador de Conjunto de Números\n")

    try:
        n = int(input("Digite a quantidade de números a serem inseridos: "))

        # Cria um objeto do analisador de conjunto de números
        analisador = AnalisadorConjuntoNumeros()

        for i in range(n):
            valor = float(input(f"Digite o {i+1}º número: "))
            analisador.adicionar_valor(valor)

        # Obtém o menor valor, o maior valor e a soma dos valores
        menor_valor = analisador.obter_menor_valor()
        maior_valor = analisador.obter_maior_valor()
        soma_valores = analisador.obter_soma_valores()

        # Exibe os resultados
        print("Menor valor:", menor_valor)
        print("Maior valor:", maior_valor)
        print("Soma dos valores:", soma_valores)

    except ValueError as ve:
        print("Erro:", str(ve))
    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
