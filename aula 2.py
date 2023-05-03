# Exemplo de operadores booleanos básicos:
print(4 > 2)
print( 4 == 2)

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

#Ex if e else

if n1 > n2:
    M = n1
    m = n2
else:
    M = n2
    m = n1

print('O maior número digitado foi: ' + str(M))
print('O menor número digitado foi: ' + str(m))

# if sem o else
# nº em módulo
n = int(input('Informe um valor para calcular em módulo: '))
if n < 0:
    n = -1 * n
print('O módulo do valor digitado é: ' + str(n))

# pg 81 livro 

'''
1. Escreva um programa que aceite os comprimentos de três lados de um triângulo como entradas. 
A saída do programa deve indicar se o triângulo é ou não um triângulo equilátero.
'''
a = int(input('Digite um lado do triângulo: '))
b = int(input('Digite outro lado do triângulo: '))
c = int(input('Digite outro lado do triângulo: '))

if a == b == c:
    print('É um triângulo equilátero.')
else:
    print('Não é um triângulo equilátero.')


'''
2. Escreva um programa que aceite os comprimentos de três lados de um triângulo como entradas. 
A saída do programa deve indicar se o triângulo é ou não um triângulo retângulo. 
Lembre-se do teorema de Pitágoras que, em um triângulo retângulo, o quadrado de um lado é igual
à soma dos quadrados dos outros dois lados.
'''

a = int(input('Digite um lado do triângulo: '))
b = int(input('Digite outro lado do triângulo: '))
c = int(input('Digite outro lado do triângulo: '))

if a ** 2 == b ** 2 + c ** 2 or b ** 2 == c ** 2 + a ** 2 or c ** 2 == b ** 2 + a ** 2:
    print('É um triângulo retângulo.')
else:
    print('Não é um triângulo retângulo.')


# pg 82 

