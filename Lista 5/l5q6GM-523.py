#Lista de Exercício 5 - Questão 6
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

class ConversorHorario:
    @staticmethod
    def converter(horas, minutos):
        if not (0 <= horas <= 23):
            raise ValueError("A hora deve estar entre 0 e 23.")
        if not (0 <= minutos <= 59):
            raise ValueError("Os minutos devem estar entre 0 e 59.")

        if horas == 0:
            horas = 12
            periodo = 'A'
        elif horas < 12:
            periodo = 'A'
        elif horas == 12:
            periodo = 'P'
        else:
            horas -= 12
            periodo = 'P'

        return horas, minutos, periodo

    @staticmethod
    def imprimir(horas, minutos, periodo):
        print(f"{horas}:{minutos:02d} {periodo}.M.")

    @classmethod
    def ler_e_converter(cls):
        while True:
            try:
                h = int(input("Insira a hora (0-23): "))
                m = int(input("Insira os minutos (0-59): "))

                hora_conv, min_conv, periodo = cls.converter(h, m)

                cls.imprimir(hora_conv, min_conv, periodo)

                resposta = input("Deseja converter outro horário? (S/N) ")
                if resposta.upper() == 'N':
                    break
            except ValueError as e:
                print(f"Erro: {e}")

ConversorHorario.ler_e_converter()
