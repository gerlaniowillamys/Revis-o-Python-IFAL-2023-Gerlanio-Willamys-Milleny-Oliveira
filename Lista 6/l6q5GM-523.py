#Lista de Exercício 6 - Questão 5
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#nome na vertical (escada invertida)

#usada para tratar erros relacionados ao formato do nome digitado pelo usuário.
class InvalidNameError(Exception):
    pass

def print_name_inverted_staircase(name):#recebe o nome digitado pelo usuário como parâmetro.
    if not name.isalpha():
        raise InvalidNameError("O nome deve conter apenas letras.") #Se houver algum caractere não alfabético, levanta uma exceção InvalidNameError
    
    for i in range(len(name), 0, -1): #Caso contrário, itera sobre cada letra do nome, começando pelo comprimento total do nome e decrementando até 1, e imprime uma substring decrescente do nome.
        print(name[:i])

def main():
    try:
        name = input("Digite seu nome: ")
        print_name_inverted_staircase(name)
    except InvalidNameError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
