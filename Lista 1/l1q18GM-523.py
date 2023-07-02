#Lista de Exercício 1 - Questão 18
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de internet (em Mbps): "))

tamanho_arquivo_bits = tamanho_arquivo * 8 * 1024 * 1024  # convertendo o tamanho do arquivo para bits
velocidade_internet_bits = velocidade_internet * 1024 * 1024  # convertendo a velocidade da internet para bits por segundo

tempo_download_segundos = tamanho_arquivo_bits / velocidade_internet_bits
tempo_download_minutos = tempo_download_segundos / 60

print("Tempo aproximado de download: {:.2f} minutos".format(tempo_download_minutos))