# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele.

n = input('Digite uma palavra: ')
print('O tipo primitivo desse valor é: ', type(n))
print('Só tem espaços? - {}'.format(n.isspace()))
print('É um número? - {}'.format(n.isnumeric()))
print('É alfabético? - ', n.isalpha())
print('É alfanumérico? - ', n.isalnum())
print('Está em maiúsculo? - ', n.isupper())
print('Está em minúsculo? - ', n.islower())
print('Está capitalizado? - ', n.isidentifier())
