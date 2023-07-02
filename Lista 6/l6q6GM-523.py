#Lista de Exercício 6 - Questão 6
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# data por extenso

class InvalidDateFormatError(Exception): #usada para tratar erros relacionados ao formato da data digitada
    pass

class InvalidDateError(Exception): # usada para erros relacionados a uma data inválida.
    pass

def get_month_name(month): #função get_month_name recebe o número do mês como parâmetro e retorna o nome do mês correspondente
    month_names = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    return month_names[month - 1]

def print_date_with_month_name(date): #recebe a data no formato "dd/mm/aaaa"
    try:
        day, month, year = map(int, date.split('/')) # divide a string da data em três partes (dia, mês e ano) usando o método split('/')
        #converte cada parte em um número inteiro usando map(int, ...)
        
        if not (1 <= month <= 12):
            raise InvalidDateError("Mês inválido.")
        
        month_name = get_month_name(month)
        
        print(f" Você nasceu em {day:02d} de {month_name} de {year}")
    except (ValueError, IndexError):
        raise InvalidDateFormatError("Formato de data inválido.")

def main():
    try:
        date = input("Data de nascimento (dd/mm/aaaa): ")
        print_date_with_month_name(date)
    except InvalidDateFormatError as e:
        print("Erro:", e)
    except InvalidDateError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
