# Aula 20 Python - FUNÇÕES

No Python usamos constantemente "funções" como

print()
input()
len()
int()
...

Todas esse comandos são "funcionalidades" da linguagem que irão executar alguma ação

Porém existem funções que não vem no python e podemos crialas

Ex:

print('=-'*30) - para não ficar repetindo este comando toda vez que preciso usalo, eu posso transformalo em uma função

Para abrir uma função usamos o def

Ex: 

def linhas():
    print('=-'*30)

Agora, linhas meu print e toda vez que eu chamar por liinhas irei executar o print, se tornou uma função 'linhas()'.capitalize

###

Além disso, a o def pode ser extremamente flexivel.

Ex:

def mensagem(msg):
    print('=-'*30)
    print(msg)
    print('=-'*30)

Neste caso eu atribui um parametrô variavel do que pode ir na mensagem.__init__

Para incluir a mensagem eu uso 'mensagem('Oi Mundo')'

'Oi Mundo' é a mensagem que sera atribuida ao 'msg'

Podemos também realizar operações

Ex:
def soma(a, b):
    s = a + b
    print(s)

soma(5, 5)
soma(3, 4)

Ou seja, eu defini uma operação dentro de minha função e depois chamei ela indicando os valores necessarios para minha operação

###

Inclusive posso  adicionar outras função, como o for 

def contador(*num): - o *num sera um pacote, onde eu posso atribuir qualquer numero de variaveis que eu desejar.
    for c in contador:
        print(c)
    tamanho = len(num) - mostrara quantos itens *num armazena

contador(3, 5)
contador(4, 5 ,7, 9)
contador(7)

O *num na realidade é um TUPLA que o python criar para armazenar os valores, ou seja, todas a funcionalidade de uma TUPLA eu posso usar neste parametro

###

Também posso usar listas - aqui vou dobrar valores

def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1


lista=[2, 4, 5, 7]
dobra(lista)
print(lista)


