#Lista de Exercício 6 - Questão 8
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#políndrome

class InvalidInputError(Exception):
    pass

def is_palindrome(text):
    try:
        if not text:
            raise InvalidInputError("Sequência vazia.")
        
        # Remover espaços e pontuação e converter para letras minúsculas
        clean_text = ''.join(char.lower() for char in text if char.isalpha())
        
        # Verificar se a sequência invertida é igual à original
        return clean_text == clean_text[::-1]
    except InvalidInputError as e:
        print("Erro:", e)
        return False

def main():
    text = input("Digite uma sequência de caracteres: ")
    print("Sequência original:", text)
    
    if is_palindrome(text):
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")

if __name__ == "__main__":
    main()
