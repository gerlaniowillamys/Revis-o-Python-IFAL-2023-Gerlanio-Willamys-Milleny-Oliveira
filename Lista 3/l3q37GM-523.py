#Lista de Exercício 3 - Questão 37
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para realizar o senso dos clientes de uma academia.

#O programa solicita o código, altura e peso de cada cliente da academia.
#A digitação dos dados é encerrada quando o usuário digita 0 (zero) no campo código.
#Ao encerrar o programa, são apresentados o código e os valores do cliente mais alto, mais baixo, mais gordo e mais magro, bem como a média das alturas e dos pesos dos clientes.

class Cliente:
    def __init__(self, codigo, altura, peso):
        self.codigo = codigo
        self.altura = altura
        self.peso = peso

if __name__ == "__main__":
    clientes = []

    while True:
        try:
            codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))
            if codigo == 0:
                break

            altura = float(input("Digite a altura do cliente (em metros): "))
            peso = float(input("Digite o peso do cliente (em kg): "))

            cliente = Cliente(codigo, altura, peso)
            clientes.append(cliente)

        except ValueError:
            print("Valor inválido. Digite novamente.")

    if len(clientes) > 0:
        cliente_mais_alto = max(clientes, key=lambda x: x.altura)
        cliente_mais_baixo = min(clientes, key=lambda x: x.altura)
        cliente_mais_gordo = max(clientes, key=lambda x: x.peso)
        cliente_mais_magro = min(clientes, key=lambda x: x.peso)

        media_alturas = sum(cliente.altura for cliente in clientes) / len(clientes)
        media_pesos = sum(cliente.peso for cliente in clientes) / len(clientes)

        print("Cliente mais alto:")
        print(f"Código: {cliente_mais_alto.codigo}, Altura: {cliente_mais_alto.altura}, Peso: {cliente_mais_alto.peso}")
        print("Cliente mais baixo:")
        print(f"Código: {cliente_mais_baixo.codigo}, Altura: {cliente_mais_baixo.altura}, Peso: {cliente_mais_baixo.peso}")
        print("Cliente mais gordo:")
        print(f"Código: {cliente_mais_gordo.codigo}, Altura: {cliente_mais_gordo.altura}, Peso: {cliente_mais_gordo.peso}")
        print("Cliente mais magro:")
        print(f"Código: {cliente_mais_magro.codigo}, Altura: {cliente_mais_magro.altura}, Peso: {cliente_mais_magro.peso}")
        print("Média das alturas dos clientes:", media_alturas)
        print("Média dos pesos dos clientes:", media_pesos)

    else:
        print("Nenhum cliente registrado.")
