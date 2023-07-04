#Lista de Exercício 6 - Questão 1
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


class ComparadorStrings:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def comparar_strings(self):
        tamanho_string1 = len(self.string1)
        tamanho_string2 = len(self.string2)

        print("Compara duas strings")
        print("String 1:", self.string1)
        print("String 2:", self.string2)
        print('Tamanho de "{}": {} caracteres'.format(self.string1, tamanho_string1))
        print('Tamanho de "{}": {} caracteres'.format(self.string2, tamanho_string2))

        if tamanho_string1 == tamanho_string2:
            print("As duas strings são de tamanhos iguais.")
        else:
            print("As duas strings são de tamanhos diferentes.")

        if self.string1 == self.string2:
            print("As duas strings possuem conteúdo igual.")
        else:
            print("As duas strings possuem conteúdo diferente.")


# Obtendo as strings do usuário
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Criando instância da classe ComparadorStrings e chamando o método comparar_strings
comparador = ComparadorStrings(string1, string2)
comparador.comparar_strings()
