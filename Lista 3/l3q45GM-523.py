#Lista de Exercício 3 - Questão 45
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#programa para verificar notas de alunos
#ao final terá um gabarito, para corrigir as questões


#Criamos uma classe SistemaProva para encapsular a lógica do programa.
class SistemaProva:
    def __init__(self):
        #O método __init__ da classe define o gabarito da prova, inicializa o contador de alunos e a lista de acertos dos alunos.
        self.gabarito = {
            '01': 'A',
            '02': 'B',
            '03': 'C',
            '04': 'D',
            '05': 'E',
            '06': 'E',
            '07': 'D',
            '08': 'C',
            '09': 'B',
            '10': 'A'
        }
        self.total_alunos = 0
        self.acertos_alunos = []
    #O método iniciar é responsável por iniciar o programa e controlar a interação com os alunos
    def iniciar(self):
        while True:
            self.total_alunos += 1
            acertos = self.verificar_respostas()
            self.acertos_alunos.append(acertos)
            
            if not self.outro_aluno():
                break
        
        self.exibir_resultados()
        self.exibir_gabarito()
    
    def verificar_respostas(self):
        acertos = 0
        for questao in range(1, 11):
            resposta_aluno = self.obter_resposta(questao)
            if resposta_aluno == self.gabarito[str(questao).zfill(2)]:
                acertos += 1
        return acertos
    
    def obter_resposta(self, questao):
        while True:
            try:
                resposta = input(f"Digite a resposta da questão {str(questao).zfill(2)}: ").upper()
                if resposta not in ['A', 'B', 'C', 'D', 'E']:
                    raise ValueError("Resposta inválida. Digite uma letra entre A e E.")
                return resposta
            except ValueError as e:
                print(e)
    
    def outro_aluno(self):
        while True:
            resposta = input("Outro aluno utilizará o sistema? (S/N): ").upper()
            if resposta in ['S', 'N']:
                return resposta == 'S'
            else:
                print("Resposta inválida. Digite S para Sim ou N para Não.")
    
    def exibir_resultados(self):
        maior_acerto = max(self.acertos_alunos)
        menor_acerto = min(self.acertos_alunos)
        media = sum(self.acertos_alunos) / self.total_alunos
        
        print(f"\nMaior Acerto: {maior_acerto}")
        print(f"Menor Acerto: {menor_acerto}")
        print(f"Total de Alunos que utilizaram o sistema: {self.total_alunos}")
        print(f"Média das Notas da Turma: {media}")
    
    def exibir_gabarito(self):
        print("\nGabarito da Prova:")
        for questao, resposta in self.gabarito.items():
            print(f"{questao} - {resposta}")


# Execução do programa
sistema = SistemaProva()
sistema.iniciar()
