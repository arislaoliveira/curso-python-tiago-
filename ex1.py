'''
1. O programa de cálculo de impostos do estudo de caso gera um número de ponto flutuante que pode mostrar mais de dois dígitos de precisão. 
Empregue a função round para modificar o pro-grama a fim de exibir no máximo dois dígitos de precisão no número de saída.
'''
imposto = float(input('Digite o cálculo de imposto do estudo de caso: '))
print(round(imposto))

'''
2. Você pode calcular a área da superfície de um cubo se souber o comprimento de uma aresta. 
Escreva um programa que recebe o comprimento de uma aresta (um inteiro) como entrada e imprime a área da superfície do cubo como saída.
'''
a = int(input('Digite a aresta do cubo em metros: '))
area_cubo = 6 * a ** 2
print('A área do cubo é {} m^3'.format(area_cubo))

'''
3. Five Star Retro Video aluga fitas VHS e DVDs para os mesmos apreciadores de discos de vinil. 
A loja aluga vídeos novos por $ 3,00 por dia e os antigos por $ 2,00 por dia. 
Escreva um programa que os funcionários da Five Star Retro Video possam utilizar para calcular o custo total do aluguel de vídeos para um cliente. 
O programa deve solicitar ao usuário o número de cada tipo de vídeo e gerar o custo total.
'''
n = int(3)
v = int(2)

tipo = input('O vídeo é novo ou velho? \n Digite N para Novo e V para Velho: ').upper()
if (tipo == 'N'):
    dias = int(input('Quantos dias o vídeo ficou alugado? '))
    print('O custo total é R$ {:.2f}'.format(n * dias))
elif (tipo == 'V'):
    dias = int(input('Quantos dias o vídeo ficou alugado? '))
    print('O custo total é R$ {:.2f}'.format(v * dias)) 
else:
    print('')

'''
4. Escreva um programa que calcula o raio de uma esfera (um número de ponto flutuante) como entrada
 e então produz o diâmetro, a circunferência, a área da superfície e o volume da esfera.
'''
import math
from math import pi

raio = float(input('Digite o raio da esfera: '))
diametro = raio * 2
circ = 2 * pi * raio
area = 4 * pi * (raio ** 2)
vol = (4 / 3) * pi * (raio ** 3)

print('Raio: {} \n Diamêtro: {} \n Circunferência: {:.2f} \n Área: {:.2f} \n Volume: {:.2f}'.format(raio, diametro, circ, area, vol))

'''
5. O movimento linear de um objeto é a massa multiplicada pela velocidade. 
Escreva um programa que aceite a massa (em quilogramas) e a velocidade (em metros por segundo) 
de um objeto como entradas e então gere seu movimento linear.
''' 
massa = float(input('Digite a massa do objeto em kg: '))
vel = float(input('Digite a velocidade do objeto em metros por segundo: '))
q = massa * vel

print('O movimento linear desse objeto é {} kg.m/s'.format(q))

'''
6. A energia cinética de um objeto em movimento é dada pela fórmula KE = (1/2)mv^2 em que m é a massa do objeto e v é a velocidade. 
Modifique o programa que você criou no Projeto 5 para que ele imprima a energia cinética do objeto, bem como seu movimento linear.
'''
m = float(input('Informe a massa do objeto: '))
v = float(input('Informe a velocidade do objeto: '))
ec = (m * v ** 2) / 2
print('A energia cinética desse objeto é {} J'.format(ec))

'''
7. Escreva um programa que calcule e imprima o número de minutos em um ano. 
'''
ano = int(365)
dia = int(24)
hora = int(60)

print('Um ano tem {} minutos'.format(ano * dia * hora))

'''
8. A luz viaja em 3*10^8 metros por segundo. 
Um ano-luz é a distância que um feixe de luz percorre em um ano. 
Escreva um programa que calcule e exiba o valor de um ano-luz.
'''
v_luz = 3*10**8
ano_seg = ano * dia * hora * 60

s = v_luz * ano_seg

print('Ano luz = {} m'.format(s))

'''
9. Escreva um programa que receba como entrada um número de quilômetros e imprima o número correspondente de milhas náuticas. 
Usar as seguintes aproximações: 
• Um quilômetro representa 1/10.000 da distância entre o Polo Norte e o Equador.
• Existem 90 graus, contendo 60 minutos de arco cada um, entre o Polo Norte e o Equador. 
• Uma milha náutica corresponde a 1 minuto de uma curva.
'''
# 1 milha naútica = 1 minuto de curva = 1 minuto de arco
# 90º x 60 minutos de arco = 5400 minutos de arco 
# distância entre o polo norte e equador: 
# 5400 minutos de arco = 10.000 km
# x minuto de arco     = 1 km 

km = float(input('Digite a distância em km: '))
mn = km/10000 * 5400

print('{} km corresponde a {} milhas náuticas'.format(km, mn))

'''
10. O pagamento semanal total de um funcionário é igual ao salário por hora multiplicado pelo número 
total de horas regulares mais qualquer pagamento de horas extras. 
O pagamento de horas extras é igual ao total de horas extras multiplicado por 1,5 vez o salário por hora. 
Escreva um programa que receba como entradas o salário por hora, o total de horas regulares 
e o total de horas extras e exiba o pagamento semanal total de um funcionário.
'''

pay = float(input('Digite o valor do salário por hora: '))
h_r = int(input('Informe o total de horas regulares trabalhadas na semana: '))
h_ext = int(input('Informe o total de horas extras trabalhadas na semana: '))

print('O salário total semanal foi R${:.2f}'.format(pay * h_r + h_ext * 1.5 * pay))