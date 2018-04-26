# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice
n = int(input('Digite um número de 1 a 5 >>> '))
nu = [1, 2, 3, 4, 5]
r = choice(nu)
if r == n:
    print('Você acertou o número > {} < sorteado pelo computador >> {} <<'.format(n, r))
else:
    print('O número escolhido > {} < foi diferente do computador >> {} <<'.format(n, r))
