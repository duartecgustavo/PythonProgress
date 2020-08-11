# Desafio 92 - Aula 19 : Programa que leia o NOME, ANO DE NASCIMENTO e o numero da CARTEIRA DE TRABALHO(aleatorio).
# E ainda, caso seja digitado 0 na CTPS, nada acontece.
# Se for digitado algo, perguntar também o ANO DE CONTRATAÇÃO e o SALARIO.
# No final mostre, TODAS AS INFOS e a IDADE(FORMATADA) e a IDADE DE APOSENTADORIA(35 anos o minimo).

from datetime import date

dados = {}

dados['nome'] = str(input('Nome: ').capitalize())

dados['nascimento'] = int(input('Data de Nascimento:'))
while dados['nascimento'] > (date.today().year - 16):
    print('Data invalida!\nVocê deve ter no minimo 16 anos.')
    del dados['nascimento']
    dados['nascimento'] = int(input('Data de Nascimento:'))

dados['CT'] = int(input('N° da Carteira (4 digitos): '))
while dados['CT'] > 9999:
    print('N° invalido!')
    del dados['CT']
    dados['CT'] = int(input('N° da Carteira: '))

if dados['CT'] == 0:
    print(f'{dados["nome"]}, você deve fazer sua Carteira de Trabalho!')
break
else:
    dados['contratacao'] = int(input('Ano de contratação: '))
    while dados['contratacao'] < dados['nascimento'] + 16 :
        print('Data invalida!\nVocê deve ter no minimo 16 anos.')
        del dados['contratacao']
        dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))

idade = date.today().year - dados["nascimento"]
anosct = date.today().year - dados['contratacao']

print('=-'*15)
print(f'Banco de Dados: {dados}')
print('=-'*15)


for key, valor in dados.items():

    # Nome
    if  key == 'nome':
        print(f'Nome: {dados["nome"]}')

    # Nascimento
    if key == 'nascimento':
        print(f'Idade: {date.today().year - dados["nascimento"]} anos')

    # Carteira
    if key == 'CT':
        print(f'N° da Carteira: {dados["CT"]}')

    # Contratação
    if key == 'contratacao':
        print(f'Contratação: {dados["contratacao"]}')

    # Salario
    if key == 'salario':
        print(f'Salário: R${dados["salario"]:.2f}')

print('=-'*15)
    # Aposentadoria
print(f'Você vai se aposentar com {(idade + 35) - anosct} anos em {dados["nascimento"] + ((idade + 35) - anosct)}.')

