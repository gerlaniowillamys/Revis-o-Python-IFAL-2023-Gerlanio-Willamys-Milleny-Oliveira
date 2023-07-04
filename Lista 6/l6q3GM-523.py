#Lista de Exercício 6 - Questão 3
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#nome na vertical

class InvalidNameError(Exception): #Definimos uma classe de exceção personalizada chamada InvalidNameError, que será usada para tratar erros relacionados ao formato do nome digitado pelo usuário.
    pass

def print_name_vertically(name): #A função print_name_vertically recebe o nome digitado pelo usuário como parâmetro. 
    if not name.isalpha(): #Antes de imprimir o nome na vertical, verifica se o nome contém apenas letras utilizando o método isalpha()
        raise InvalidNameError("O nome deve conter apenas letras.") #Se houver algum caractere não alfabético, levanta uma exceção InvalidNameError
    
    for letter in name:
        print(letter)

def main():
    try:
        name = input("Digite seu nome: ")
        print_name_vertically(name)
    except InvalidNameError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()

