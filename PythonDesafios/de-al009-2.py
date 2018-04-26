# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex digite um número: 1834
# unidade : 4
# dezena: 3
# centena: 8
# milhar: 1
num = input('Digite um número de 0 a 9999: ')
print('A unidade é >', num[3])
print('A dezena  é >', num[2])
print('A centena é >', num[1])
print('O milhar  é >', num[0])