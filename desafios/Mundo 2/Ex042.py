# Desafio 42 - Aula 12 : Refazer  Desasfio 35 e mostrar qual o tipo do triangulo.
# A/ Equilatero.
# B/ Isósceles.
# C/ Escaleno.

print('\033[32mATENÇÃO! VAMOS MONTAR UM TRIÂNGULO!!!\033[m')

a = int(input('Digite a primeira medida: '))
b = int(input('Digite a segunda medida: '))
c = int(input('Digite a terceira medida: '))

if a < b + c and b < a + c and c < b + a:
    print('\033[34mTemos um triangulo!\033[m')
    if a==b==c:
        print('Este triângulo é \033[32mEQUILATERO\033[m! Pois possui todos os lados iguais.')
    elif a==b or a==c or b==c:
        print('Neste caso este triângulo possui dois lados iguais, portanto é \033[32mISÓSCELES\033[m!')
    else:
        print('Todos os lados são diferentes portante temos um triângulo \033[32mESCALENO\033[m!')
else:
    print('\033[31mNão temos um triângulo!\033[m')