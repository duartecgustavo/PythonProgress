# Desafio 59 - Aula 14 : Programa que leia dois numeros e me apresente um painel de opções:
# [1] SOMAR / [2] MULTIPLICAR / [3] MAIOR / [4] NOVOS NUMEROS / [5] SAIR DO PROGRAMA

print('\033[32m-\033[m'*50)
print(f'{"PRIMEIRO MENU":^50}')
print('\033[32m-\033[m'*50)

print('\033[34mQuero que você me diga dois numero\033[m')
escolha = 4
opcao = ''

while escolha == 4:
    num1 = int(input('1° numero: '))
    num2 = int(input('2° numero: '))

    print('\033[32m-\033[m'*50)
    print(f'{"MENU":^50}')
    print('\033[32m-\033[m'*50)

    print('[1] - SOMAR')
    print('[2] - MULTIPLICAR')
    print('[3] - MAIOR')
    print('[4] - NOVOS NUMEROS')
    print('[5] - SAIR DO PROGRAMA')


    escolha = int(input('Sua escolha: '))

    if escolha == 1:
        print(f'A soma de {num1} + {num2} é {num1+num2}.')
        opcao = str(input('Deseja continuar[S/N]?'))
        if opcao in 'Ss':
            escolha =4
    elif escolha == 2:
        print(f'A multiplicação entre {num1} * {num2} é {num1*num2}.')
        opcao = str(input('Deseja continuar[S/N]?'))
        if opcao in 'Ss':
            escolha =4
    elif escolha == 3:
        print(f'O maior numero entre {num1} e {num2} é {max(num1, num2)}')
        opcao = str(input('Deseja continuar[S/N]? '))
        if opcao in 'Ss':
            escolha =4
    elif escolha == 4:
        print('Informe novamente os numeros.')
    else:
        print('Tchau...')
    
    print(escolha)
print('Fim do programa.')