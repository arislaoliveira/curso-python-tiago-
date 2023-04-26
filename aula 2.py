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