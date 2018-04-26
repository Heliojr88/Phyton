# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
lista = [n1, n2, n3]
if n1 > n2 > n3:
    print('{} maior número'.format(n1))
else:
    print()