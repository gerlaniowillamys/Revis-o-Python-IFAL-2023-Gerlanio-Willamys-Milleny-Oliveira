#Lista de Exercício 6 - Questão 7
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#contagem de espaçamentos e vogais


class InvalidInputError(Exception): #usada para tratar erros relacionados à entrada inválida.
    pass

def count_spaces_and_vowels(sentence): #recebe a frase informada pelo usuário como parâmetro.
    try: #Dentro de um bloco try-except, a função realiza as seguintes ações:
        if not sentence:
            raise InvalidInputError("Frase vazia.") #Verifica se a frase é vazia. Se for, levanta uma exceção InvalidInputError.

        space_count = sentence.count(" ") #Conta a quantidade de espaços em branco na frase usando o método count(" ").
        vowel_count = sum(sentence.lower().count(vowel) for vowel in "aeiou") #Converte a frase para letras minúsculas usando o método lower()

#conta a quantidade de ocorrências de cada vogal usando a função count() e um loop for

#usada para somar todas as contagens de vogais, sum ( )

        return space_count, vowel_count
    except InvalidInputError as e:
        print("Erro:", e)
        return None, None #função None retorna para as contagens.

def main():
    sentence = input("Digite uma frase: ")
    space_count, vowel_count = count_spaces_and_vowels(sentence)

    if space_count is not None and vowel_count is not None:
        print("Quantidade de espaços em branco:", space_count)
        print("Quantidade de vogais:", vowel_count)

if __name__ == "__main__":
    main()
