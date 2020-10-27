# Desafio 115 - Aula 23 : Crie um pequeno sistema de modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simplês.
# O sistema vai ter 2 opçãoes: Cadastrar e ver pessoas cadastradas.

import Ex115.Modulos115
from time import sleep

arq = "cursoemvideo.txt" # ARQUIVO PARA SER CRIADO

#SE O ARQUIVO NÃO EXISTIR, CRIA O ARQUIVO
if not Ex115.Modulos115.arquivo(arq):
    Ex115.Modulos115.criarArquivo(arq)


while True:
    resposta = Ex115.Modulos115.menu(['CADASTRAR PESSOA', 'VER LISTA DE PESSOAS', 'SAIR DO PROGRAMA'])

    # MOSTRAR LISTA DE PESSOAS
    if (resposta == 1):
        Ex115.Modulos115.titulo('LISTA DE PESSOAS')
        Ex115.Modulos115.lerArquivo(arq)

    # CADASTRAR PESSOAS
    elif (resposta == 2):
        Ex115.Modulos115.titulo('CADASTRAR PESSOA')
        nome = str(input('Nome:'))
        idade = Ex115.Modulos115.leiaInt('Idade: ')
        Ex115.Modulos115.cadastrar(arq, nome, idade)

    #SAIR DO PROGRAMA
    elif (resposta == 3):
        print('Saindo do sistema...')
        sleep(2)
        break

    else:
        print('Erro: digite uma opção valida!')

print('Fim do programa!')
