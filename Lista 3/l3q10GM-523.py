#Lista de Exercício 3 - Questão 10
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para gerar os números inteiros dentro de um intervalo

class GeradorNumerosInteiros:
    def gerar_numeros_inteiros(self, inicio, fim):
        # Verifica se os números fornecidos estão em ordem crescente
        if inicio > fim:
            inicio, fim = fim, inicio

        # Gera e imprime os números inteiros no intervalo
        for numero in range(inicio + 1, fim):
            print(numero, end=' ')

def main():
    print("Programa para gerar os números inteiros dentro de um intervalo.\n")

    try:
        # Solicita a entrada dos números
        inicio = int(input("Digite o primeiro número: "))
        fim = int(input("Digite o segundo número: "))

        # Cria um objeto do gerador de números inteiros e chama a função para gerar os números
        gerador = GeradorNumerosInteiros()
        gerador.gerar_numeros_inteiros(inicio, fim)

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar apenas números inteiros.")

if __name__ == '__main__':
    main()
