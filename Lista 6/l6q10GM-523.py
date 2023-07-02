#Lista de Exercício 6 - Questão 10
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Número por Extenso
#Este programa solicita ao usuário a digitação de um número até 99
#e imprime-o por extenso.

class NumeroPorExtenso: #representa um número e possui métodos para obter o extenso das unidades e das dezenas
    def __init__(self, numero):
        self.numero = numero

    def _obter_extenso_unidades(self, numero): #se o número digitado é válido e retorna o extenso correspondente
        unidades = {
            '0': 'zero',
            '1': 'um',
            '2': 'dois',
            '3': 'três',
            '4': 'quatro',
            '5': 'cinco',
            '6': 'seis',
            '7': 'sete',
            '8': 'oito',
            '9': 'nove'
        }
        return unidades[numero]

    def _obter_extenso_dezenas(self, numero):
        dezenas = {
            '10': 'dez',
            '11': 'onze',
            '12': 'doze',
            '13': 'treze',
            '14': 'quatorze',
            '15': 'quinze',
            '16': 'dezesseis',
            '17': 'dezessete',
            '18': 'dezoito',
            '19': 'dezenove',
            '2': 'vinte',
            '3': 'trinta',
            '4': 'quarenta',
            '5': 'cinquenta',
            '6': 'sessenta',
            '7': 'setenta',
            '8': 'oitenta',
            '9': 'noventa'
        }
        return dezenas[numero]

    def obter_extenso(self):
        if self.numero.isdigit() and 0 <= int(self.numero) <= 99:
            if len(self.numero) == 1:
                return self._obter_extenso_unidades(self.numero)
            elif len(self.numero) == 2:
                if self.numero[0] == '1':
                    return self._obter_extenso_dezenas(self.numero)
                else:
                    extenso = self._obter_extenso_dezenas(self.numero[0])
                    if self.numero[1] != '0':
                        extenso += ' e ' + self._obter_extenso_unidades(self.numero[1])
                    return extenso
        else:
            raise ValueError('Número inválido.')


def main():
    numero_digitado = input("Digite um número até 99: ")

    try:
        numero_extenso = NumeroPorExtenso(numero_digitado)
        extenso = numero_extenso.obter_extenso()
        print(extenso)
    except ValueError as e:
        print("Ocorreu um erro:", str(e))


if __name__ == '__main__':
    main()
6