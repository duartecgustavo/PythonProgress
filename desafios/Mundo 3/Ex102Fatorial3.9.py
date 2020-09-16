# Desafio 102 - Aula 21: Programa que tenha a função fatorial() e que receba dois valores.
# O primeiro deve indicar o numero  a ser calculado.
# O segundo deeverá mostrar um valor lógico (opcional) indicando se será mostrado ou não o processo de calculo do fatorial.


def fatorial(num=0, show=0):

    f = 1
    for c in range(num, 0, -1):
        f*=c
        if show == True:
            print(c, end=' ')
            print('x ' if c != 1 else '= ',end='')
    return f

while True:

    print('-'*50)
    num = int(input('Numero: '))
    esc = str(input('Digite "SIM" para mostrar a expressão ou "NÃO" para finalizar: ')).lower()[0]
    if esc in 's':
        esc = True
    else:
        esc = False
    print(fatorial(num,esc))

    choice = str(input('Quer continuar? [S/N]')).upper()[0]
    while choice not in 'SN':
        choice=str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]
    if choice in 'N':
        break    

print('FIm do Programa!')
