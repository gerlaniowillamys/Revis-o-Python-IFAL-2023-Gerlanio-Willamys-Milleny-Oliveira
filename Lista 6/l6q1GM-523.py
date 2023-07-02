#Lista de Exercício 6 - Questão 1
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


# Função para comparar duas strings
def comparar_strings(string1, string2):
    tamanho_string1 = len(string1)
    tamanho_string2 = len(string2)

    print("Compara duas strings")
    print("String 1:", string1)
    print("String 2:", string2)
    print('Tamanho de "{}": {} caracteres'.format(string1, tamanho_string1))
    print('Tamanho de "{}": {} caracteres'.format(string2, tamanho_string2))

    if tamanho_string1 == tamanho_string2:
        print("As duas strings são de tamanhos iguais.")
    else:
        print("As duas strings são de tamanhos diferentes.")

    if string1 == string2:
        print("As duas strings possuem conteúdo igual.")
    else:
        print("As duas strings possuem conteúdo diferente.")


# Obtendo as strings do usuário
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Chamando a função para comparar as strings
comparar_strings(string1, string2)
