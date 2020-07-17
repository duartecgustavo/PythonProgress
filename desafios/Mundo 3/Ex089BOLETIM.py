# Desadio 89 - Aula 18 : Programa que leia o nome e duas notas de varios alunos. Depois guarde tudo em uma çista composta.
# Mostre o Boletim contendo a média de cada aluno.
# Permita que o usuario possa ver a nota de cada aluno individualmente.

nome=[]
notas=[]
lista=[]
count=0

while True:
    nome.append(str(input('Diga seu nome: ')))

    #validando notas
    notas.append(float(input('Diga sua nota de Matematica: ')))
    if notas[0] > 10:
        notas.pop()
        notas.append(float(input('\033[31mDiga uma nota valida!\033[m Sua nota de Matematica: ')))

    notas.append(float(input('Diga sua nota de Português: ')))
    if notas[1] > 10:
        notas.pop()
        notas.append(float(input('\033[31mDiga uma nota valida!\033[m Sua nota de Português: ')))

    #add nomes na lista e junto de nomes outra lista com as notas
    lista.append(nome[:])
    lista[count].append(notas[:])
    #add média junto a lista individual de cada nome
    lista[count].append((notas[0]+notas[1])/2)
    nome.clear()
    notas.clear()
    count+=1

    print('-'*25)
    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        print('-='*35)
        count=0
        break
    print('-'*35)

print('No.  NOME.          MÉDIA.')
for aluno in lista:
    count+=1
    print(f'{count:<5}{aluno[0].capitalize():.<15}{aluno[2]:.2f}')

while True:
    choice = str(input(f'Deseja ver a nota de algum aluno especifico?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!Quer ver as notas?[S/N] ')).upper()[0]
    if choice in 'N':
        break

    alunoesp = int(input('Qual o NUMERO do aluno que vc deseja ver as notas: '))
    while True:
        if alunoesp-1 >= len(lista):
            alunoesp = int(input(f'Não existem {alunoesp} alunos cadastradros, apenas {len(lista)}.\nQual o NUMERO do aluno que vc deseja ver as notas: '))
        else: break

    print('-' * 25)
    print(f'{lista[alunoesp-1][0].capitalize():<20}Notas')
    for pos, cont in enumerate(lista):
        if pos == alunoesp-1:
            print(f'{"Matematica":.<20}{cont[1][0]:<5.2f}')
            print(f'{"Português":.<20}{cont[1][1]:<5.2f}')
            print('-' * 35)

print('Fim do programa.')