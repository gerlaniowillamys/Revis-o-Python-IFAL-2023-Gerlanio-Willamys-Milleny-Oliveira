#Lista de Exercício 6 - Questão 4
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#nome na vertical em escada

#InvalidNameError, usada para tratar erros relacionados ao formato do nome digitado pelo usuário
class InvalidNameError(Exception):
    pass

def print_name_staircase(name): #recebe o nome digitado pelo usuário como parâmetro.
    if not name.isalpha():
        raise InvalidNameError("O nome deve conter apenas letras.")
    
    for i in range(len(name)):
        print(name[:i+1])

def main():
    try:
        name = input("Digite seu nome: ")
        print_name_staircase(name)
    except InvalidNameError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
