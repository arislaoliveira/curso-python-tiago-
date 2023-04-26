a = int(input('Digite um lado do triângulo: '))
b = int(input('Digite outro lado do triângulo: '))
c = int(input('Digite outro lado do triângulo: '))

if a ** 2 == b ** 2 + c ** 2: #or b ** 2 == c ** 2 + a ** 2 or c ** 2 == b ** 2 + a ** 2:
    print('É um triângulo retângulo.')
else:
    print('Não é um triângulo retângulo.')
