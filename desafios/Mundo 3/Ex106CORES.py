# Desafio 106 - Aula 21: Programa que utilize o 'interactive help' do Python.
# O usuario irá digitar o comando e o terminal deve retornar sua explicação.
# Para saisr digite 'FIM!'

from time import sleep

# Dict com cores

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'lilas':'\033[35m',
         'branco':'\033[7:30m'}

# Função principal

def bibli(msg):
    sleep(0.8)
    titulo(f'Acessandoo o manual do comando \'{msg}\'', cor = 'lilas')
    sleep(0.5)

    print(cores['branco'])
    help(msg)
    print(cores['limpa'])

# Função com cores

def titulo(msg, cor = 'limpa'):
    print(cores[cor], end='')
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(cores['limpa'], end='')

#Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHelp',cor = 'azul')
    msg = str(input(('Função ou Biblioteca: '))).lower()
    if msg in 'fim':
        break
    else:
        bibli(msg)

titulo(msg = 'FIM DO PROGRAMA!', cor = 'limpa')
