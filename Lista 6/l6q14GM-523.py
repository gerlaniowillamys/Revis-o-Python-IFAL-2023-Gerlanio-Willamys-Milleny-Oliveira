#Lista de Exercício 6 - Questão 14
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Leet Speak Generator
#Este programa converte um texto para a grafia Leet Speak.

class LeetSpeakGenerator:
    def __init__(self):
        self.leet_dict = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            's': '5',
            't': '7'
        }

    def converter_para_leet(self, texto):
        texto_leet = ''
        for letra in texto:
            if letra.lower() in self.leet_dict:
                texto_leet += self.leet_dict[letra.lower()]
            else:
                texto_leet += letra
        return texto_leet

    def executar(self):
        print('Leet Speak Generator')
        texto = input('Digite um texto: ')
        texto_leet = self.converter_para_leet(texto)
        print('Texto convertido para Leet Speak:', texto_leet)


def main():
    leet_generator = LeetSpeakGenerator()
    leet_generator.executar()


if __name__ == '__main__':
    main()
