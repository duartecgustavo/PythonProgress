# Desafio 63 - Aula 14 : Sequencia de FIBONACCI.
# Leia um numero e mostre a sequencia até este numero
count = 2
t1 = 0
t2 = 1

print('=-'*30)
num = int(input('Numero para sequencia de FIBONACCI: '))
print('=-'*30)

print(f'{t1} -> {t2}', end='')
while count < num:
    count +=1
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
print(' -> Fim')
