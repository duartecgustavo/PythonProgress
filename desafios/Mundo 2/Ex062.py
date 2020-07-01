# Desafio 62 - Aula 14 : Melhorar o DEASFIO 61 e perguntara se deseja adicionar mais termos a PA.
count = 0
fim = 10

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

while count < fim:
    inicio+=razao
    count +=1
    print(inicio, end='')
    if count == fim:
        escolha = str(input('\nQuer adicionar mais termos? '))
        if escolha in 'Ss':
            pluss = int(input('Quantos termos deseja adicionar? '))
            fim += pluss
        else:
            count = fim
    print(' -> ' if count < fim else '',end='')
print(f'Fim\nNo total apareceram na tela {count} termos.')