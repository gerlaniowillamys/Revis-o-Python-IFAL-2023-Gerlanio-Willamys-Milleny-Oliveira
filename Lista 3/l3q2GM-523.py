#Lista de Exercício 3 - Questão 2
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda

# Programa de validação de nome de usuário e senha

class Usuario:
    def __init__(self, nome_usuario, senha):
        self.nome_usuario = nome_usuario
        self.senha = senha

    def validar_senha(self):
        # Verifica se a senha é igual ao nome de usuário
        if self.senha == self.nome_usuario:
            raise ValueError("A senha não pode ser igual ao nome de usuário.")

        # Caso a validação seja bem-sucedida
        print("Nome de usuário e senha registrados com sucesso!")


while True:
    try:
        # Solicita o nome de usuário e senha ao usuário
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        # Cria uma instância da classe Usuario
        usuario = Usuario(nome_usuario, senha)

        # Realiza a validação da senha
        usuario.validar_senha()
        
        # Encerra o loop
        break

    except ValueError as error:
        # Exibe a mensagem de erro em caso de validação falha
        print(f"Erro: {error}. Tente novamente.")
