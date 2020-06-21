# Desafio 68 - Aula 15 : Jogo do PAR ou IMPAR.
from random import randint
from time import sleep
count = 0

print('-='*30)
print(f'{"DESAFIO DO PAR ou IMPAR":^60}')
print('=-'*30)

while True:

    #Escolha do jogador
    print('\nFaça sua escolha!')
    while True:
        choice = str(input('\n\033[31mPar\033[m ou \033[34mImpar\033[m?[P/I] ')).upper()
        if choice not in 'PI':
            print('Opção invalida!')
        else: break
    num = int(input('\nQual o valor?[1/10] '))

    #Escolha da maquina
    pc = randint(1, 10)
    soma = pc+num

    print('\n\033[31mPAR\033[m')
    print('-'*10)
    sleep(0.5)
    print('ouu')
    print('-'*10)
    sleep(0.5)
    print('\033[34mIMPAR\033[m')
    print('-'*10)
    sleep(0.5)

    if soma % 2 == 0:
        comp = 'Par'
    elif soma % 2 == 1:
        comp = 'Impar'

    if choice == 'P' and soma % 2 == 0:
        count += 1
        print(f'Você \033[34mVENCEU!!!\033[m')
        print(f'A escolha do PC foi {pc} e a do jogador foi {num} o que dá {soma} que é \033[31mPAR!\033[m')
    elif choice == 'I' and soma % 2 == 1:
        count += 1
        print(f'Você \033[34mVENCEU!!!\033[m')
        print(f'A escolha do PC foi {pc} e a do jogador foi {num} o que dá {soma} que é \033[34mIMPAR!\033[m')
    else:
        print(f'Você \033[31mPERDEU!\033[m')
        print(f'A escolha do PC foi {pc} e a do jogador foi {num} o que dá {soma} que é {comp}!')


    while True:
        continuar = str(input('Quer continuar?[S/N] ')).upper()
        if continuar not in 'SN':
            print('Opção invalida!')
        else: break

    if continuar not in 'S':
        break


print(f'\033[31mEND GAME!\033[m\nVocê venceu {count} vezes;')