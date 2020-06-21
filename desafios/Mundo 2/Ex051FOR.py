# Desafio 51 - Aula 13 : Programa que leia o primeiro termo e a razão de uma progressão artimatica, no final mostre os 10 primeiros termos des PA.

inicio = (int(input('Digite o primeiro numero: ')))
razao = (int(input('Digite a razão desta PA: ')))
formula = inicio + (10-1) * razao
print(formula)
for c in range(inicio, formula + razao, razao):
    print(c, end=' -> ')
print('FIM!')

# Forma que eu fiz:

'''conta = 0
inicio = int(input('Me diga o numero que vai começar: '))
razao = int(input('Agora me diga a razão desta PA: '))
for c in range (inicio, 1000, razao):
    conta = conta + 1
    if conta < 11:
        print(c, end=' -> ')
print('ABABOU')'''