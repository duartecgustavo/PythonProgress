# Desafio 83 - Aula 17 : Programa onde o usuario digite uma EXPRESSÃO que use PARENTESES.
# O programa deve analizar se a expressão esta com todos os parenteses corretamente abertos e fechados ou não.

listaparenteses = listaresto = []
count = diferenca = 0

while True:
    exp = str(input('Digite uma expressão: '))
    print('_'*50)

    for peca in exp:
        if peca in '()':
            count +=1
            listaparenteses.append(peca)
        else:
            listaresto.append(peca)

    esquerda = listaparenteses.count('(')
    direita = listaparenteses.count(')')

    if count >=1 :
        if esquerda == direita:
            print('A expressão está correta.')
        else:
            print('A expressão está errada!')
            if esquerda > direita:
                diferenca = esquerda-direita
                print(f'Está faltando {diferenca} parenteses como este ")"')
            else:
                diferenca = direita-esquerda
                print(f'Está faltando {diferenca} parenteses como este "("')
    else:
        print('Aparentemente a expressão está correta.')

    print('_'*45)
    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'S':
        del listaparenteses[:]
        del listaresto[:]
    else: break
print('Fim do programa')
