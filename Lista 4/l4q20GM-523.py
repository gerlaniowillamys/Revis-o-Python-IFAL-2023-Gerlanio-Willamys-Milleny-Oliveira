#Lista de Exercício 4 - Questão 20
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


def main():
    salarios = []
    abonos = []
    valor_minimo = 100
    total_gasto = 0
    valor_maximo = 0
    num_colaboradores = 0
    num_minimo = 0

    print("Projeção de Gastos com Abono\n")
    print("============================\n")

    while True:
        try:
            salario = float(input("Salário: "))
        except ValueError:
            print("Informe um valor válido.\n")
            continue

        if salario == 0:
            break

        salarios.append(salario)

        if salario <= valor_minimo:
            abono = valor_minimo
            num_minimo += 1
        else:
            abono = salario * 0.2

        abonos.append(abono)
        total_gasto += abono

        if abono > valor_maximo:
            valor_maximo = abono

        num_colaboradores += 1

    print("\nSalário          - Abono")
    for i in range(num_colaboradores):
        print(f"R$ {salarios[i]:.2f}       - R$ {abonos[i]:.2f}")

    print(f"\nForam processados {num_colaboradores} colaboradores")
    print(f"Total gasto com abonos: R$ {total_gasto:.2f}")
    print(f"Valor mínimo pago a {num_minimo} colaboradores")
    print(f"Maior valor de abono pago: R$ {valor_maximo:.2f}")


if __name__ == "__main__":
    main()
