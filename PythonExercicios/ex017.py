# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
''' co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto oposto adjacente: '))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi)) '''

from math import hypot
cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
hip = hypot(cop, cad)
print('A hipotenusa do triangulo é {:.2f}'.format(hip))