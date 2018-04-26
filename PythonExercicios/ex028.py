# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep # Biblioteca time função sleep faça um intervalo de tempo até executar ou processo
computador = randint(0, 5) # Faz o computador sortear o numero
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número estou pensando?? '))
print('PENSANDOOOOOOO')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você acertou o mesmo número')
else:
    print('GANHEI!! Tente novamente!!!')
