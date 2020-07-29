## Python - Listas 	:bookmark_tabs:
> a linguagem **Python** possui 3 modelos de listas

* Tuplas ()
* Listas []
* Bibliotecas {}

---
### TUPLAS - Listas Fixas :pushpin:

> começando pelas **Tuplas ()** que é um modelo de lista **fixa**, ou seja, não podem ser alteradas

* TUPLAS SÃO IMUTÁVEIS!

As tuplas são definidas com **()**:

#### Exemplo:

`lanche = ('hamburguer','suco','brigadeiro', 'bala')` - defini uma tupla

`print(lanche[::-1])` - estou apresentando a Tupla de *trás para frente*

`print(len(lanche))` - apresento *quantos elementos* tem a Tupla com o comando `len()`

```
for comida in lanche:

    print(comida, end = ' ') - usando o FOR, mostro a lista sem os parenteses
```

> a manipulação do que o usuario irá ver é igual a **manipulação de STRINGS**

---
### Métodos :abacus:

* `len()` - vai **ler quantos valores** tem a tupla - `print(len(tupla))`

* `.count()` - apresenta quantos **valores especificos** que eu indiquei estão na tupla - `print(b.count(6))`

* `.index()` - vai me dizer a **posição que o valor indicado** aparece - `print(b.index(5))`

* `sorted` - **organiza** a tupla por **ordem numerica ou alfabetica** - `print(sorted(lanche))`

---
### Adicionando itens :heavy_plus_sign:
> podemos adicionar itens a lista unindo funções e metodos da seguinte forma

`lanche = tuple(int(input('Diga a comida que vai no lanche: ')) for comida in range(1,5)`

Acima, **defini a tupla** *lanche* com `tuple`, com o `input` indiquei que **um valor entrará na tupla** e depois com o `for` indiquei **quantas vezes** o a pergunta deve ser apresentada.

---
### Comando ENUMERATE :inbox_tray:

> posso indicar a posição de algo na tupla e o valor presente nesta posição de uma só vez

`for posicao, comida in enumerate(lanche):`

Sempre possuirá dois indices, o **primeiro indica a posição** do item que o `for` está. O **segundo o que está naquela posição**.

```
        print(f'Comi {posicao+1}° a {comida}') - Comi 1° hamburguer
        
        print(f'Comi {posicao+1}° a {comida}') - Comi 2° suco
```

#### Outra forma de encontrar um item da tupla:

```
for comida in range(0, len(lanche)):

    print(f'Eu quero come {lanche[comida]} na posição {comida}'
```

Já aqui vai sempre mostrar o lanche porem o 'comida' vai determinar qual valor sera mostrado

---
### Deletendo tupla - `DEL()` :x:

> com o comando `DEL()` você pode **deletar basicamente qualquer coisa** em Python

`del (lanche)` - deletará a tupla

### Somando Tuplas()

```
a = (1, 2, 3)

b = (5, 7, 6, 4, 5)
```
`print(a + (b[-1::-1]))` - ao **somar tuplas** o python simplesmente as une


[:arrow_backward:](https://github.com/duartecgustavo/Python-Progress/blob/master/conteudo/indice.md)


