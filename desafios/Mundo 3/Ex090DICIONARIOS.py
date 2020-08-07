# Desafio 90 - Aula 19 :  Programa que leia o NOME e a MÉDIA de um aluno apenas. Guarde também a SITUAÇÃO em um DICIONARIO.
# Depois mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('Seu nome: '))

aluno['Média'] = float(input('Sua média: '))
while aluno['Média'] < 0 or aluno['Média'] > 10:
    aluno['Média'] = float(input('Impossivel!\nSua média: '))

if aluno['Média'] <= 5:
    aluno['Situação'] = ("REPROVADO!")
else:
    aluno['Situação'] = ("APROVADO!")

print('=-'*20)

for indice, cont in aluno.items():
    print(f'{indice} é {cont}.')