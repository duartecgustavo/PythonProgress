# Desafio 103 - Aula 21: Programa que tenha a função chamada ficha(), que receba 2 parâmetros opcionais: 
# NOME do jogador e quantos GOLS ele fez.
# O programa deve mostrar a ficha com os dados do jogar, mesmo que nenhum valor tenha sido informado.

def ficha(nome ='', gols = ''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gols.'
        
nome = str(input('Nome do jogador: ')).capitalize()
gols = str(input('Gols marcados: '))

print(ficha(nome,gols))