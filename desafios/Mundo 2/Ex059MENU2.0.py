# Desafio 59 - Aula 14 : Programa que leia dois numeros e me apresente um painel de opções:
# [1] SOMAR / [2] MULTIPLICAR / [3] MAIOR / [4] NOVOS NUMEROS / [5] SAIR DO PROGRAMA

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:

    print(''' [ 1 ] SOMAR
     [ 2 ] MULTIPLICAR
     [ 3 ] MAIOR
     [ 4 ] NOVOS NUMEROS
     [ 5 ] SAIR DO PROGRAMA''')

    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        print(f'A soma é {n1+n2}.')
    elif opcao == 2:
        print(f'A multiplicação é {n1*n2}.')
    elif opcao == 3:
        print(f'O maior numero é {max(n1,n2)}')
    elif opcao == 4:
        print('Informe os numeros novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção invalida, etente novamente.')

print('Fim do programa!')