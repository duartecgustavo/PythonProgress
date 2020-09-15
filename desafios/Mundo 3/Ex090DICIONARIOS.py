# Desafio 90 - Aula 19 :  Programa que leia o nome e a média, analize sua situação (APROVADO/REPROVADO) e armazene tudo em um dicionario.
# Depois mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('Seu nome: '))

aluno['Média'] = float(input('Sua média: '))
while aluno['Média'] < 0 or aluno['Média'] > 10:
    aluno['Média'] = float(input('Impossivel!\nSua média correta: '))

if aluno['Média'] <= 5:
    aluno['Situação'] = ("REPROVADO!")
else:
    aluno['Situação'] = ("APROVADO!")

print('=-'*20)

print(aluno)
#for indice, cont in aluno.items():
 #   print(f'{indice} é {cont}.')
