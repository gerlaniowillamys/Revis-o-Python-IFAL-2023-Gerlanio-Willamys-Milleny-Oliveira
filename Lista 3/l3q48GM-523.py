#Lista de Exercício 3 - Questão 48
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#função inverter_numero recebe um número como entrada e retorna o número invertido
def inverter_numero(numero):
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
    return int(numero_invertido)

#Na função main, solicitamos ao usuário que digite um número inteiro positivo.
def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            raise ValueError("O número deve ser positivo.") #verificamos se o número é positivo e, caso contrário, lançamos um erro usando ValueError
        
        numero_invertido = inverter_numero(numero)#Chamamos a função inverter_numero para obter o número invertido e o exibimos na tela.
        print("Número invertido:", numero_invertido)
    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()
