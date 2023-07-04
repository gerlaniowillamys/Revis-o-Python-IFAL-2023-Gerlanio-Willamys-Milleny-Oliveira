#Lista de Exercício 3 - Questão 12
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para gerar a tabuada de um número entre 1 e 10

class GeradorTabuada:
    def gerar_tabuada(self, numero):
        # Verifica se o número está dentro do intervalo válido
        if numero < 1 or numero > 10:
            raise ValueError("O número deve estar entre 1 e 10.")

        # Gera e imprime a tabuada
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

def main():
    print("Gerador de Tabuada\n")

    try:
        # Solicita a entrada do número da tabuada
        numero = int(input("Digite um número de 1 a 10: "))

        # Cria um objeto do gerador de tabuada e chama a função para gerar a tabuada
        gerador = GeradorTabuada()
        gerador.gerar_tabuada(numero)

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar apenas números inteiros.")

    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()
