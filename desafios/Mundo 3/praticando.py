# Desafio 90 - Aula 19 :  Programa que leia o NOME e a MÉDIA de um aluno apenas. Guarde também a SITUAÇÃO em um DICIONARIO.
# Depois mostre o conteúdo da estrutura na tela.

aluno =  {}

aluno['nome'] = str(input('Nome: '))

aluno['media'] = float(input('Média: '))
while aluno['media'] >10 or aluno['media'] < 0:
    aluno['media']= float(input('Opção invalida!\nMédia: '))

if aluno['media'] >= 5:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'

print(f'O aluno {aluno["nome"]} tirou média {aluno["media"]} e foi {aluno["situação"]}.')