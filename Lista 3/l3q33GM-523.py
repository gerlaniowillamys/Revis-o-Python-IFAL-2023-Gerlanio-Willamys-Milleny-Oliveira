#Lista de Exercício 3 - Questão 33
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Programa para análise de temperaturas.

#O programa lê um conjunto indeterminado de temperaturas informadas pelo usuário.

#Ao final, exibe a menor temperatura, a maior temperatura e a média das temperaturas.

class AnalisadorTemperaturas:
    def __init__(self):
        self.temperaturas = []

    def ler_temperaturas(self):
        while True:
            try:
                temperatura = float(input("Digite uma temperatura (ou 0 para finalizar): "))
                if temperatura == 0:
                    break
                self.temperaturas.append(temperatura)
            except ValueError:
                print("Temperatura inválida. Digite um valor numérico válido.")

    def obter_menor_temperatura(self):
        return min(self.temperaturas)

    def obter_maior_temperatura(self):
        return max(self.temperaturas)

    def calcular_media_temperaturas(self):
        return sum(self.temperaturas) / len(self.temperaturas)

if __name__ == "__main__":
    analisador = AnalisadorTemperaturas()

    analisador.ler_temperaturas()  # Lê as temperaturas informadas pelo usuário

    if len(analisador.temperaturas) > 0:
        menor_temperatura = analisador.obter_menor_temperatura()
        maior_temperatura = analisador.obter_maior_temperatura()
        media_temperaturas = analisador.calcular_media_temperaturas()

        print(f"Menor temperatura: {menor_temperatura}")
        print(f"Maior temperatura: {maior_temperatura}")
        print(f"Média das temperaturas: {media_temperaturas:.2f}")
    else:
        print("Nenhuma temperatura foi informada.")

