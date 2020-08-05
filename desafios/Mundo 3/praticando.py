# Desadio 89 - Aula 18 : Programa que leia o NOME e DUAS NOTAS de VARIOS ALUNOS. Depois guarde tudo em uma lista composta.
# Mostre o Boletim contendo a média de cada aluno.
# Permita que o usuario possa ver a nota de cada aluno individualmente.

aluno=[]
banco=[]
media = 0

while True:
    aluno.append(str(input('Diga o nome do aluno: ')).capitalize())

    aluno.append(float(input('Diga a nota de Matematica: ')))
    while aluno[1] > 10 or aluno[1] < 0:
        aluno.pop()
        aluno.append(float(input('Nota invalida!\nDiga sua nota de Matematica: ')))

    aluno.append(float(input('Diga a nota de Português: ')))
    while aluno[2] > 10 or aluno[2] < 0:
        aluno.pop()
        aluno.append(float(input('Nota invalida!\nDiga sua nota de Português: ')))
    aluno.append((aluno[1]+aluno[2]/2))

    banco.append(aluno[:])
    aluno.clear()

    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        break

while True:
    print('=-'*25)
    print(f'{"No":<7}{"Aluno":<8}{"Média":>15}')
    for pos, nome in enumerate (banco):
        print(f'{pos+1:<7}{nome[0]:<8}{nome[3]:>15.2f}')

    choice = str(input('Quer ver a nota especifica de um dos alunos?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer ver a nota especifica de um os alunos?[S/N] ')).upper()[0]
    if choice in 'N':
        break
    else:

        choicealuno = int(input('Diga o numero do aluno que vc deseja ver a nota: '))
        while choicealuno-1 >= len(banco) or choicealuno < 0:
            choicealuno = int(input('Opção invalida!\nDiga o numero do aluno que vc deseja ver a nota: '))
        
        print(banco[choicealuno-1][0])
        print(f'Nota de Português {banco[choicealuno-1][2]:.>16.2f}')
        print(f'Nota de Matemática {banco[choicealuno-1][1]:.>15.2f}')


