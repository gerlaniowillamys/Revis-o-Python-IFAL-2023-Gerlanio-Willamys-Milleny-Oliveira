#Lista de Exercício 1 - Questão 2 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

def obter_numero():
    while True:
        try:
            numero = int(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def exibir_numero(numero):
    print("O número informado foi", numero)

if __name__ == "__main__":
    try:
        numero = obter_numero()
        exibir_numero(numero)
    except Exception as e:
        print("Ocorreu um erro:", e)
