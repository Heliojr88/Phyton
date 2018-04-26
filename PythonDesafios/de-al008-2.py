# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
hip = hypot(cop, cad)
print('A hipotenusa do triangulo é {:.2f}'.format(hip))