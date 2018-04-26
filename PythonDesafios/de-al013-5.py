# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
soma = 0
cont = 0
n1 = int(input('Digite um número de 1 a 6: '))
if n1 % 2 == 0:
    for c in range(0, 7, 2):
        if c % 2 == 0:
            soma += c
            cont += 1
    print('A soma dos {} valores somente os pares é de {}'.format(cont, soma))
elif n1 >= 7:
    print('Número digitado inválido, tente novamente')
else:
    print('Número digitado é ímpar')
