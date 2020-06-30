# Desafio 57 - Aula 14 : Leia o sexo de uma pessoa, porém só aceite os valore 'M' ou 'F'.
# Caso contrario peça a digitação correta.

sex = str(input('Informe seu sexo[M/F]: ')).upper()

while sex != 'M' and sex != 'F': # while sex not in 'FfMm':
    print(f'{sex} é diferente de [M/F], digite novamente',end=' ')
    sex = str(input('seu sexo[M/F]: ')).upper()

print(f'Sexo {sex} registrado.')
