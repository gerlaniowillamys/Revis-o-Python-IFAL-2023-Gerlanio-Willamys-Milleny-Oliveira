#Lista de Exercício 6 - Questão 9
#Dupla: 2021316110- Gerlânio Willamys e 2021317055 - Milleny Oliveira 
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Neste código, usamos a expressão regular re.sub(r'[^0-9]', '', cpf) para remover todos os caracteres não numéricos do CPF, mantendo apenas os dígitos. Em seguida, verificamos se o CPF tem 11 dígitos e se todos os dígitos são iguais (o que não é permitido em um CPF válido).
#Depois, calculamos os dois dígitos verificadores do CPF usando o algoritmo apropriado. Finalmente, comparamos os dígitos verificadores calculados com os dígitos verificadores fornecidos no CPF digitado pelo usuário. Se eles forem iguais, o CPF é considerado válido; caso contrário, é considerado inválido.

import re

def validar_cpf(cpf):
    # Remover caracteres de formatação do CPF
    cpf = re.sub(r'[^0-9]', '', cpf)

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    # Calcular o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    soma += digito1 * 2
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    # Verificar se os dígitos verificadores estão corretos
    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False

# Solicitar o CPF ao usuário
cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

# Verificar se o CPF é válido
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")