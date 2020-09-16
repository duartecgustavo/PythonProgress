# Desafio 101 - Aula 21: Programa que valide o voto pela idade do individuo.
# Deve possuir uma função chamada voto(), que vai receber o parâmetro Ano_de_Nascimento.
# Depois retornara um valor literal que pode ser NEGADO, OPCIONA ou OBRIGATÓRIO nas eleições.

def voto(ano = 0):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ',end=' ')
    ''' def voto() quando chamada retornará a situação do indivíduo em reçalção ao voto.'''
    if ano <= 0 or ano > date.today().year:
        condicao = 'ANO INVÁLIDO'
    elif idade < 18:
        condicao = 'VOTO NEGADO!'
    elif idade < 65:
        condicao = 'VOTO OBRIGATÓRIO!'
    else:
        condicao = 'VOTO OPCIONAL!'
    return condicao

while True:

    print('-'*50)
    ano = int(input('Ano de Nascimento: '))
    print(voto(ano))

    choice = str(input('Quer continuar? [S/N]')).upper()[0]
    while choice not in 'SN':
        choice=str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]
    if choice in 'N':
        break

print('Programa Finalizado!')
