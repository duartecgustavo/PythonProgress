# Desafio 63 - Aula 14 : Sequencia de FIBONACCI, leia um numero 'n' e mostre na tela a sequencia até este numero

print('=-'*30)
num = int(input('Numero para sequencia de FIBONACCI: '))
print('=-'*30)

count = 2
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
while count < num:
    count +=1
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
print(' -> Fim')
