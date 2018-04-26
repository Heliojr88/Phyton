# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan
a = int(input('Digite o ângulo: '))
print('O ângulo {}° tem o cosseno {:.3}, o seno {:.3} e a tangente {:.3} !!!'.format(a, cos(a), sin(a), tan(a)))
