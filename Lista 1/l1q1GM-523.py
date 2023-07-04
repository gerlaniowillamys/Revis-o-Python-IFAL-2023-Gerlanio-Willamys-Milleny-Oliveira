#Lista de Exercício 1 - Questão 1 
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

def exibir_mensagem():
    print("Alô mundo")

if __name__ == "__main__":
    try:
        exibir_mensagem()
    except Exception as e:
        print("Ocorreu um erro:", e)
