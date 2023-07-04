#Lista de Exercício 7 - Questão 9
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def criar_ponto():
    try:
        x = float(input("Digite a coordenada x do ponto: "))
        y = float(input("Digite a coordenada y do ponto: "))
        return Ponto(x, y)
    except ValueError:
        print("Coordenadas inválidas. Usando ponto padrão (0, 0).")
        return Ponto()


def alterar_retangulo(retangulo):
    try:
        print("Valores atuais do retângulo:")
        retangulo.ponto_inicial.imprimir()
        print(f"Largura: {retangulo.largura}")
        print(f"Altura: {retangulo.altura}")

        x = float(input("Digite a nova coordenada x do ponto inicial: "))
        y = float(input("Digite a nova coordenada y do ponto inicial: "))
        retangulo.ponto_inicial = Ponto(x, y)
        retangulo.largura = float(input("Digite a nova largura do retângulo: "))
        retangulo.altura = float(input("Digite a nova altura do retângulo: "))
    except ValueError:
        print("Valores inválidos. O retângulo não foi alterado.")


def imprimir_centro(retangulo):
    centro = retangulo.encontrar_centro()
    print("Centro do retângulo:")
    centro.imprimir()


def exibir_menu():
    print("\n===== MENU =====")
    print("1. Alterar valores do retângulo")
    print("2. Imprimir centro do retângulo")
    print("0. Sair")


if __name__ == '__main__':
    ponto_inicial = criar_ponto()
    largura = 0
    altura = 0

    try:
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
    except ValueError:
        print("Valores inválidos. Usando largura e altura padrão (0).")

    retangulo = Retangulo(ponto_inicial, largura, altura)

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            alterar_retangulo(retangulo)
        elif opcao == '2':
            imprimir_centro(retangulo)
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")
