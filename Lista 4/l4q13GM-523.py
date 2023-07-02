#Lista de Exercício 4 - Questão 13
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#Calcular a média anual das temperaturas e mostrar as temperaturas acima da média e seus respectivos meses.

class Mes:
    def __init__(self, nome, temperatura):
        self.nome = nome
        self.temperatura = temperatura

def main():
    try:
        meses = []  # Lista para armazenar os objetos Mes

        # Entrada das temperaturas médias de cada mês
        for i in range(12):
            nome_mes = obter_nome_mes(i+1)
            temperatura = float(input(f"Informe a temperatura média de {nome_mes}: "))

            mes = Mes(nome_mes, temperatura)
            meses.append(mes)

        # Cálculo da média anual das temperaturas
        soma_temperaturas = sum(mes.temperatura for mes in meses)
        media_anual = soma_temperaturas / len(meses)

        # Exibição das temperaturas acima da média anual e seus respectivos meses
        print("Temperaturas acima da média anual:")
        for mes in meses:
            if mes.temperatura > media_anual:
                print(f"{mes.nome}: {mes.temperatura:.1f}")

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar uma temperatura válida.")

def obter_nome_mes(numero):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[numero - 1]

if __name__ == "__main__":
    main()
