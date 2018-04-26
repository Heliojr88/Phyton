# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
from time import sleep
print('-=-' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 8)
a = float(input('Digite a medida 1: '))
b = float(input('Digite a medida 2: '))
c = float(input('Digite a medida 3: '))
print('ANALISANDO...')
sleep(3)
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM FORMAR um triângulo')
else:
    print('Os segmentos NÂO PODEM FORMAR um triângulo')
