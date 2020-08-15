# Desafio 92 - Aula 19 : Programa que leia o NOME, ANO DE NASCIMENTO e o numero da CARTEIRA DE TRABALHO(aleatorio).
# Caso seja digitado 0 na CTPS, nada acontece.
# Se for digitado algo, perguntar também o ANO DE CONTRATAÇÃO e o SALARIO.
# No final mostre, TODAS AS INFOS, IDADE(FORMATADA) e a IDADE DE APOSENTADORIA(35 anos o minimo).

from datetime import date

dados = dict()

dados['Nome'] = str(input('Nome: ').capitalize())

nasc = int(input('Ano de Nascimento: '))
while True:
    if nasc > date.today().year:
        print(f'{"ATENÇÃO":-^30}')
        print(f'Data invalida!\nDigite o ano correto.')
        nasc = int(input('Ano de Nascimento:'))
        print(f'{"-"*30}')
    elif date.today().year >= nasc > (date.today().year - 16):
        print(f'{"ATENÇÃO":-^30}')
        print(f'Você ainda não tem idade para trabalhar!\nVolte comm 16 anos.')
        print(f'{"-"*30}')
        break
    else:
        dados['Idade'] = date.today().year - nasc
        break


ctps = str(input('Numero da CTPS [5 digitos]: '))
while ctps != '0':
    if len(ctps) != 5:
        print(f'{"ATENÇÃO":-^30}')
        print(f'Dados invalidos!\nA sua Carteira de Trabalho só pode conter 5 digitos!')
        ctps = str(input('Numero da CTPS: '))
        print(f'{"-"*30}')
    else:
        dados['CTPS'] = ctps
        break
if ctps == '0':
    dados['CTPS'] = ctps
else:
    contratacao = int(input('Ano de Contratação: '))
    while contratacao <= (nasc + 16) or contratacao > (nasc + 70):
        print(f'{"ATENÇÃO":-^30}')
        print(f'Informação invalida!')
        print(f'{"-"*30}')
        contratacao = int(input('Ano de Contratação: '))
    dados['Contratação'] = contratacao

    dados['Salário'] = float(input(f'Salário: R$'))

    aposentadoria = dados['Idade'] + ((dados['Contratação'] + 35) - date.today().year)
    dados['Aposentadoria'] = aposentadoria

print('=-'*15)
print(f'Banco de Dados: {dados}')
print('=-'*15)

for key, valor in dados.items():   

    print(f'{key}: {valor}')    
