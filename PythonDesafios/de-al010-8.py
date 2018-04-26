# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('-=-' * 8)
print('ANALISADOR DE TRIÂNGULO')
print('-=-' * 8)
a = float(input('Digite a medida 1: '))
b = float(input('Digite a medida 2: '))
c = float(input('Digite a medida 3: '))
ra = (b - c) < a < b + c
rb = (a - c) < b < a + c
rc = (a - b) < c < a + b
final = ra == rb == rc
if final:
    print('As medidas {}cm, {}cm e {}cm PODEM FORMAR um triângulo'.format(a, b, c))
else:
    print('As medidas {}cm, {}cm e {}cm NÃO PODEM FORMAR um triângulo'.format(a, b, c))
print('obrigado!!!')