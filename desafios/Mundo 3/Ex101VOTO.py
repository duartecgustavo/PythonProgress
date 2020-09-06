# Desafio 101 - Aula 21: Programa que valide o voto pela idade.
# Deve possuir uma FUNÇÃO() chamada voto() que vai receber  o parametro Ano de Nascimento
# Depois retornara um valor literal que pode ser NEGADO, OPCIONAL, OBRIGATÓRIO nas eleições

from datetime import date

def voto(ano = 0):
    if idade < 18:
        print('VOTO NEGADO!')
    elif idade < 65:
        print('VOTO OBRIGATÓRIO!')
    else:
        print('VOTO OPCIONAL!')

while True:

    print('-'*50)

    ano = int(input('Ano de Nascimento: '))

    idade = date.today().year - ano
    print(f'Com {idade} anos: ',end=' ')
    voto(ano)

    choice = str(input('Quer continuar? [S/N]')).upper()[0]
    while choice not in 'SN':
        choice=str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]
    if choice in 'N':
        break