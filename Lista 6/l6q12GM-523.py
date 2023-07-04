#Lista de Exercício 6 - Questão 12
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#Valida e Corrige Número de Telefone
#Este programa lê um número de telefone e corrige o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.

class Telefone:
    def __init__(self, numero):
        self.numero = numero

    def _remover_formatacao(self):
        return self.numero.replace('-', '')

    def _adicionar_formatacao(self, numero):
        return f'{numero[:4]}-{numero[4:]}'

    def _corrigir_numero(self):
        numero_sem_formatacao = self._remover_formatacao()

        if len(numero_sem_formatacao) == 7:
            numero_corrigido = '3' + numero_sem_formatacao
            self.numero = self._adicionar_formatacao(numero_corrigido)

    def validar_e_corrigir(self):
        if not self.numero.isdigit():
            raise ValueError('Número de telefone deve conter apenas dígitos.')

        if len(self.numero) == 8 or len(self.numero) == 9:
            self._corrigir_numero()
            print('Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
            print('Telefone corrigido sem formatação:', self._remover_formatacao())
            print('Telefone corrigido com formatação:', self.numero)
        else:
            raise ValueError('Número de telefone inválido.')


def main():
    print('Valida e Corrige Número de Telefone')
    telefone = input('Telefone: ')

    try:
        telefone_objeto = Telefone(telefone)
        telefone_objeto.validar_e_corrigir()
    except ValueError as e:
        print('Ocorreu um erro:', str(e))


if __name__ == '__main__':
    main()
