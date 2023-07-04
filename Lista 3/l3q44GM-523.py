#Lista de Exercício 3 - Questão 44
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#programa para fazer votação de eleição

#A classe EleicaoPresidencial é criada para representar a eleição presidencial
class EleicaoPresidencial:
    def __init__(self):
        self.candidatos = {
            1: 'José',
            2: 'João',
            3: 'Maria',
            4: 'Ana'
        }
        self.votos = {
            'candidatos': {candidato: 0 for candidato in self.candidatos},
            'nulos': 0,
            'brancos': 0
        }
        self.total_votos = 0
    #O método receber_votos é responsável por receber os votos dos eleitores. Ele utiliza um loop para solicitar ao usuário que digite o código do candidato (ou '0' para encerrar)
    def receber_votos(self):
        while True:
            voto = int(input("Digite o código do candidato (ou '0' para encerrar): "))
            
            if voto == 0:
                break
            elif voto in self.candidatos:
                self.votos['candidatos'][voto] += 1
            elif voto == 5:
                self.votos['nulos'] += 1
            elif voto == 6:
                self.votos['brancos'] += 1
            else:
                print("Código de voto inválido. Tente novamente.")
            
            self.total_votos += 1
    
    def exibir_resultados(self):
        print("Resultado da Eleição Presidencial")
        print("------------------------------")
        
        for candidato, nome in self.candidatos.items():
            total_votos_candidato = self.votos['candidatos'][candidato]
            percentual_votos_candidato = (total_votos_candidato / self.total_votos) * 100
            print(f"{nome}: {total_votos_candidato} votos ({percentual_votos_candidato:.2f}%)")
        
        total_votos_nulos = self.votos['nulos']
        percentual_votos_nulos = (total_votos_nulos / self.total_votos) * 100
        
        total_votos_brancos = self.votos['brancos']
        percentual_votos_brancos = (total_votos_brancos / self.total_votos) * 100
        
        print(f"Votos Nulos: {total_votos_nulos} votos ({percentual_votos_nulos:.2f}%)")
        print(f"Votos em Branco: {total_votos_brancos} votos ({percentual_votos_brancos:.2f}%)")
        print("------------------------------")
        print(f"Total de votos: {self.total_votos}")


eleicao = EleicaoPresidencial()
eleicao.receber_votos()
eleicao.exibir_resultados()
