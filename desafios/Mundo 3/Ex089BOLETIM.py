# Desadio 89 - Aula 18 : Programa que leia o NOME e DUAS NOTAS de VARIOS ALUNOS. Depois guarde tudo em uma lista composta.
# Mostre o Boletim contendo a média de cada aluno.
# Permita que o usuario possa ver a nota de cada aluno individualmente.

nome=[]
notas=[]
lista=[]
count=0

while True:
    nome.append(str(input('Diga seu nome: ')))

    #cadastrando e validando notas
    notas.append(float(input('Diga sua nota de Matematica: ')))
    if notas[0] > 10:
        notas.pop()
        notas.append(float(input('\033[31mDiga uma nota valida!\033[m Sua nota de Matematica: ')))

    notas.append(float(input('Diga sua nota de Português: ')))
    if notas[1] > 10:
        notas.pop()
        notas.append(float(input('\033[31mDiga uma nota valida!\033[m Sua nota de Português: ')))

    #add nomes na lista
    lista.append(nome[:])
    #add as notas a lista, dentro da lista individual de cada nome
    lista[count].append(notas[:])
    #add média junto a lista individual de cada nome
    lista[count].append((notas[0]+notas[1])/2)
    
    #limpando as listas nome e notas
    nome.clear()
    notas.clear()
    
    #o 'count' indica a posição que cada lista com o nome representa dentro da lista principal
    count+=1

    print('-'*25)
    #validando
    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        print('-='*35)
        count=0
        break
    print('-'*35)

print('No.  NOME.          MÉDIA.')

#printando o a média de cada aluno em formato de boletim
for aluno in lista:
    count+=1
    print(f'{count:<5}{aluno[0].capitalize():.<15}{aluno[2]:.2f}')

#validando
while True:
    choice = str(input(f'Deseja ver a nota de algum aluno especifico?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!Quer ver as notas?[S/N] ')).upper()[0]
    if choice in 'N':
        break

    #notas de cada aluno individualmente
    alunoesp = int(input('Qual o NUMERO do aluno que vc deseja ver as notas: '))
    #validadando numero do aluno com o numero de alunos cadastrados
    while True:
        if alunoesp-1 >= len(lista):
            alunoesp = int(input(f'Não existem {alunoesp} alunos cadastradros, apenas {len(lista)}.\nQual o NUMERO do aluno que vc deseja ver as notas: '))
        else: break

    #printando em formato de lista as notas do aluno especificado
    print('-' * 25)
    print(f'{lista[alunoesp-1][0].capitalize():<20}Notas')
    for pos, cont in enumerate(lista):
        if pos == alunoesp-1:
            print(f'{"Matematica":.<20}{cont[1][0]:<5.2f}')
            print(f'{"Português":.<20}{cont[1][1]:<5.2f}')
            print('-' * 35)

print('Fim do programa.')
