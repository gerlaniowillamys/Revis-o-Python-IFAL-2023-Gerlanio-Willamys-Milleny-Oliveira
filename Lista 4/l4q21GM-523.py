#Lista de Exercício 4 - Questão 21
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#O programa inicia solicitando os dados dos carros em um loop. 
#Para cada carro, o usuário insere o nome e o consumo em km por litro

def main():
    carros = [] #Os nomes dos carros são armazenados na lista carros
    consumo = []  #Os consumos são armazenados na lista consumo

    print("Comparativo de Consumo de Combustível\n")

    for i in range(5):
        nome = input(f"Veículo {i+1}\nNome: ")
        km_por_litro = float(input("Km por litro: "))
        carros.append(nome)
        consumo.append(km_por_litro)

    print("\nRelatório Final")
    for i in range(5):
        consumo_1000km = 1000 / consumo[i]
        custo = consumo_1000km * 2.25
        print(f"{i+1} - {carros[i]:<15} - {consumo[i]:>4.1f} - {consumo_1000km:>6.1f} litros - R$ {custo:.2f}")

    indice_menor_consumo = consumo.index(min(consumo)) #determinado o índice do carro com o menor consumo utilizando a função min aplicada à lista consumo
    print(f"\nO menor consumo é do {carros[indice_menor_consumo]}")


if __name__ == "__main__":
    main()
