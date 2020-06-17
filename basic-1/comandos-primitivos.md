### Tipos de comandos `primitivos`:

`int = NUMEROS INTEIROS: 2, 0, -5, 7685, 13, 42`

`flaot = NUMEROS REAIS: 4.5, 2.234, 0.75646, -15.234, 3.14`

`bool = DOIS VALORES: True and False (importante começar com letra maiscula)`

`str = STRING COMUM: 'OLÁ' (Tudo que estiver entre aspas '')`

**EX:**

`a = input('Digite qualquer coisa aqui: ')`

`print(type(a))` - aqui irá me dizer que categoria o que foi digitado se enquadra.

Abaixo se o que foi digitado é ou não cada tipo primitivo.

```print('{} está em minusculo?'.format(a), a.islower())
print('{} está em maiusculo??'.format(a), a.isupper())
print('{} é somento numero?'.format(a), a.isnumeric())
print('{} é somente letras?'.format(a), a.isalpha())
print('{} são numeros ou letras?'.format(a), a.isalnum())```
