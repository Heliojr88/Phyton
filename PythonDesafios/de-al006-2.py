# Faça um programa que leia algo pelo teclado e motre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele.
n = int(input('Digite um número: '))
nfloat = float(input('Digite um outro número: '))
st = str(input('Digite qualquer coisa: '))
print('Número no formato primitivo: {}'.format(n), type(n))
print('Segundo número no formato primitivo: {}'.format(nfloat), type(nfloat))
print('Essas palavras estão no formato primitivo: {}'.format(st), ',do tipo: ', type(st))
n1 = input('Digite um número: ')
l = input('Digite seu nome: ')
print('O número digitado é:', n1.isnumeric())
print('Seu nome digitado é: ', l.isalpha())
