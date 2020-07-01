# Desafio 61 - Aula 14 : Refaça o DESAFIO 51 usando o WHILE.
count = 0

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

while count < 10:
    print(f'{inicio}', end=' ')
    inicio+=razao
    count+=1


'''inicio = int(input('Numero que vai começar: '))
razao = int(input('Razão da PA: '))
fim = inicio + (10-1) * razao
while inicio < fim+1:
    print(inicio, end=' ')
    inicio += razao
print('FIM')'''