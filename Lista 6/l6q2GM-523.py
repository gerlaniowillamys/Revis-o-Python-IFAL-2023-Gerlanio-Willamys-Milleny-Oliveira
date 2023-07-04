#Lista de Exercício 6 - Questão 2
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#nome invertido ( em maiúsculo)

#Definimos uma classe de exceção personalizada chamada InvalidNameError, que será usada para tratar erros relacionados ao formato do nome digitado pelo usuário.
class InvalidNameError(Exception):
    pass

def reverse_name(name): #A função reverse_name recebe o nome digitado pelo usuário como parâmetro
    if not name.isalpha(): #Antes de realizar a inversão, verifica se o nome contém apenas letras utilizando o método isalpha().
        raise InvalidNameError("O nome deve conter apenas letras.") #Se houver algum caractere não alfabético, levanta uma exceção InvalidNameError.
    
    
    #Caso contrário, inverte o nome utilizando a sintaxe de fatiamento ([::-1])
    reversed_name = name[::-1].upper() #converte todas as letras para maiúsculas com o método upper(). O nome invertido é retornado.
    return reversed_name

def main(): #função main é responsável por executar o programa principal
    try:
        name = input("Digite seu nome: ")
        reversed_name = reverse_name(name)
        print("Nome invertido:", reversed_name)
    except InvalidNameError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()

