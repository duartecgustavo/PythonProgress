# Desafio 61 - Aula 14 : Refaça o DESAFIO 51 usando o WHILE.

'''inicio = int(input('Numero que vai começar: '))
razao = int(input('Razão da PA: '))
fim = inicio + (10-1) * razao
while inicio < fim+1:
    print(inicio, end=' ')
    inicio += razao
print('FIM')'''

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

c = 0
while c < 10:
    print(f'{inicio}', end=' ')
    inicio+=razao
    c+=1