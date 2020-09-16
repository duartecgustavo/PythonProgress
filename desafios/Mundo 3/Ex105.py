# Desafio 105 - Aula 21: Programa que tenha a função notas() que pode  receber varias notas de alunos e retornará um dicionario com as seguintes informações.
# Quantidade de notas.
# A maior Nota.
# A menor Nota.
# A média da Turma.
# A situação.

# Adicionar os docstrings

def notas(*num, sit = False):
    """
    quant = quantidade de notas
    maior = maior nota digitado
    menor = menor nota digitado
    media = media das notas
    """
    soma = 0

    quant = len(num)
    maior = max(num)
    menor = min(num)

    for c in num:
        soma+=c
    media = soma/quant
    # media = sum(num)/len(num)

    if media >= 7:
        sit = 'Boa!'
    elif 5 < media < 7:
        sit = 'Medio'
    else:
        sit = 'Ruim!'
    
    dict = {'Quantidade': quant, 'Maior': maior, 'Menor': menor, 'Média': media, 'Situação': sit}
    return dict


resp = notas(9.9, 8, 5.6, 3)
print(resp)