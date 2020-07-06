# Desafio 83 - Aula 17 : Programa onde o usuario digite uma EXPRESSÃO que use PARENTESES.
# O programa deve analizar se a expressão esta com todos os parenteses corretamente abertos e fechados ou não.
# Versão Guanabara

valor = str(input('Diga uma expressão: '))
pilha = []

for simb in valor:
    if simb == '(':
        pilha.append('(')
    else:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta!')
else:
    print('A opção está errada.')