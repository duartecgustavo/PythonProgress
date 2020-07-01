# Desafio 73 - Aula 16 : Crie uma TUPLA com os 20 primeiros colocados da tabela do Brasileirão, depois mostre:
# A - Os 5 primeiros colocados / B - Os quatro ultimos colocados / C - Lista em ordem alfabetica / Em que posição na tabela está o time do SANTOS?
# Junto ao painel interativo para que a pessoas possa escolher o que ela quer.
from time import sleep
count = invert = 0

print('-='*30)
print(f'{"ANALIZE TIMES DE LOL BRASILEIROS":^60}')
print('=-'*30)

timeslol = ('Paingaming','CNB Sports','Santos','Flamengo','intz','Kabum','Vivo Keyd','Furia','RedCanids','IDM')


print(f'{"O QUE VOCê DESEJA SABER?":^60}')
print('-=' * 30)

while True:

    print('[1] - PRIMEIROS COLOCADOS'
          '\n[2] - ULTIMOS COLOCADOS'
          '\n[3] - LISTA EM ORDEM ALFABETICA'
          '\n[4] - POSIÇÃO DO SEU TIME'
          '\n[5] - VER TABELA COMPLETA'
          '\n[6] - SAIR DO PROGRAMA')

    print('_'*33)
    choice = int(input('Diga sua opção: '))
    print('_'*43)

    # validando escolha
    while choice > 6 or choice < 1:
        choice = int(input('\033[31mOpção invalida!\033[m\nDiga sua opção:'))

    sleep(1)

    # escolha 1

    if choice == 1:
        print(f'Os primeiros colocados na CBLOL 2020 são: ')
        for n1 in range(0,3):
            print(f'{n1+1}° - {timeslol[n1]}')

    # escolha 2

    if choice == 2:
        invert = len(timeslol)
        print(f'Os ultimos colocados são: ')
        for n2 in range(-1,-4,-1):
            invert-=1
            print(f'{invert}° - {timeslol[n2]}')

    # escolha 3

    if choice == 3:
        timealfa = sorted(timeslol)
        for n3 in timealfa:
            count+=1
            print(f'{count}° - {n3}')

    # escolha 4

    if choice == 4:

        usertime = str(input('Qual seu time? '))
        usertimeseparado = usertime.lower().split()
        usertimejunto = (''.join(usertimeseparado))
        for time in timeslol:
            count+=1
            testeseparado = time.lower().split()
            testejunto = ''.join(testeseparado)

            if testejunto == usertimejunto:
                print(f'{usertime.capitalize()} apareçe na {count}° posição!')
                count-=1
            if count == len(timeslol):
                print(f'{usertime.capitalize()} não está entre os melhores times de LOL do Brasil!')

    # escolha 5

    if choice == 5:
        for lol in timeslol:
            print(f'{timeslol.index(lol)+1}° - {lol}')

    # escolha 6

    if choice == 6:
        break

    count= 0
    sleep(2)
    print('='*43)

print('Fim do programa!')