# Desafio 59 - Aula 14 : Programa que leia dois numeros e me apresente um painel de opções:
# [1] SOMAR / [2] MULTIPLICAR / [3] MAIOR / [4] NOVOS NUMEROS / [5] SAIR DO PROGRAMA

escolha = 0
opcao = ''

while escolha != 5:
    num1 = int(input('1° numero: '))
    num2 = int(input('2° numero: '))

    print('\033[32m-\033[m'*10)
    print(f'{"MENU":<10}')
    print('\033[32m-\033[m'*10)

    print('[1] - SOMAR')
    print('[2] - MULTIPLICAR')
    print('[3] - MAIOR')
    print('[4] - NOVOS NUMEROS')
    print('[5] - SAIR DO PROGRAMA')


    escolha = int(input('Sua escolha: '))

    if escolha == 1 or escolha == 2 or escolha == 3:
        if escolha == 1:
            print(f'A soma de {num1} + {num2} é {num1+num2}.')    

        elif escolha == 2:
            print(f'A multiplicação entre {num1} * {num2} é {num1*num2}.')
                
        elif escolha == 3:
            print(f'O maior numero entre {num1} e {num2} é {max(num1, num2)}')

        opcao = str(input('Deseja continuar[S/N]?')).lower()[0]

        if opcao in 'n':
            escolha = 5
            

    elif escolha == 4:
        print('Informe novamente os numeros.')
    
print('Fim do programa.')