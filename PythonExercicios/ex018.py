# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
ag = float(input('Digite o ângulo desejado: '))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(ag, math.sin(math.radians(ag))))
print('O ângulo de {}° tem o COSENO de {:.2f}'.format(ag, math.cos(math.radians(ag))))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(ag, math.tan(math.radians(ag))))