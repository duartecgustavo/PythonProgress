
lista = []
nota= 0
soma = 0
23
for c in range(0,4):
    nota = int(input(f'Diga o {c+1}° numero: '))
    lista.append(nota)

print(lista)
for v in lista:
    if v % 2 == 0:
        soma+=v
print(soma)
