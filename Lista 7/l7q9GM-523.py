#Lista de Exercício 7 - Questão 9
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Classe Ponto com os atributos x e y
class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


# Classe Retangulo com os atributos largura e altura
class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Função para criar um objeto da classe Ponto
def criar_ponto():
    x = float(input("Digite a coordenada x do ponto: "))
    y = float(input("Digite a coordenada y do ponto: "))
    return Ponto(x, y)


# Função para alterar os valores do retângulo
def alterar_retangulo(retangulo):
    print("Valores atuais do retângulo:")
    retangulo.ponto_inicial.imprimir()
    print(f"Largura: {retangulo.largura}")
    print(f"Altura: {retangulo.altura}")

    x = float(input("Digite a nova coordenada x do ponto inicial: "))
    y = float(input("Digite a nova coordenada y do ponto inicial: "))
    retangulo.ponto_inicial = Ponto(x, y)
    retangulo.largura = float(input("Digite a nova largura do retângulo: "))
    retangulo.altura = float(input("Digite a nova altura do retângulo: "))


# Função para imprimir o centro do retângulo
def imprimir_centro(retangulo):
    centro = retangulo.encontrar_centro()
    print("Centro do retângulo:")
    centro.imprimir()


# Função para exibir o menu
def exibir_menu():
    print("\n===== MENU =====")
    print("1. Alterar valores do retângulo")
    print("2. Imprimir centro do retângulo")
    print("0. Sair")


# Programa principal
if __name__ == '__main__':
    ponto_inicial = criar_ponto()
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

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
