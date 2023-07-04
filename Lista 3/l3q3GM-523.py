#Lista de Exercício 3 - Questão 3
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa para ler e validar informações de uma pessoa

class Validador:
    @staticmethod
    def validar_nome(nome):
        # Valida se o nome possui mais de 3 caracteres
        if len(nome) <= 3:
            raise ValueError("O nome deve ter mais de 3 caracteres.")

    @staticmethod
    def validar_idade(idade):
        # Valida se a idade está entre 0 e 150
        idade = int(idade)
        if not 0 <= idade <= 150:
            raise ValueError("A idade deve estar entre 0 e 150.")

    @staticmethod
    def validar_salario(salario):
        # Valida se o salário é maior que zero
        salario = float(salario)
        if salario <= 0:
            raise ValueError("O salário deve ser maior que zero.")

    @staticmethod
    def validar_sexo(sexo):
        # Valida se o sexo é 'f' ou 'm'
        sexo = sexo.lower()
        if sexo not in ['f', 'm']:
            raise ValueError("O sexo deve ser 'f' ou 'm'.")

    @staticmethod
    def validar_estado_civil(estado_civil):
        # Valida se o estado civil é 's', 'c', 'v' ou 'd'
        estado_civil = estado_civil.lower()
        if estado_civil not in ['s', 'c', 'v', 'd']:
            raise ValueError("O estado civil deve ser 's', 'c', 'v' ou 'd'.")


class Pessoa:
    def __init__(self, nome, idade, salario, sexo, estado_civil):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.sexo = sexo
        self.estado_civil = estado_civil

    @staticmethod
    def ler_e_validar_informacao(mensagem, validacao):
        # Função para ler e validar uma informação
        while True:
            try:
                valor = input(mensagem)
                validacao(valor)
                return valor
            except ValueError as e:
                print(e)

    @classmethod
    def ler_informacoes(cls):
        # Função para ler as informações de uma pessoa
        nome = cls.ler_e_validar_informacao("Digite o nome (maior que 3 caracteres): ", Validador.validar_nome)
        idade = cls.ler_e_validar_informacao("Digite a idade (entre 0 e 150): ", Validador.validar_idade)
        salario = cls.ler_e_validar_informacao("Digite o salário (maior que zero): ", Validador.validar_salario)
        sexo = cls.ler_e_validar_informacao("Digite o sexo ('f' para feminino ou 'm' para masculino): ", Validador.validar_sexo)
        estado_civil = cls.ler_e_validar_informacao("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado): ", Validador.validar_estado_civil)
        return cls(nome, idade, salario, sexo, estado_civil)

    def exibir_informacoes(self):
        # Função para exibir as informações válidas da pessoa
        print("Informações válidas:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self.salario)
        print("Sexo:", self.sexo)
        print("Estado Civil:", self.estado_civil)


pessoa = Pessoa.ler_informacoes()
pessoa.exibir_informacoes()
