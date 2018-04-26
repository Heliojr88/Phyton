# Crie um programa que faça o computador jogar jokenpô com você
import emoji
from time import sleep
from random import randint
print('\033[34m*=* \033[m' * 7)
print(emoji.emojize('\033[33m Jogo do Jokenpô\033[m \033[31m:facepunch:\033[m \033[36m:hand:\033[m \033[35m:v:\033[m', use_aliases=True))
print('\033[34m*=* \033[m' * 7)
print('\033[7;31;40mTente ganhar da máquina!!!\033[1;31;40m     BOA SORTE       \033[m')
print('Suas opções')
print('\033[1;31m[ 0 ]\033[m - \033[1;31mPEDRA\033[m')
print('\033[1;35m[ 1 ]\033[m - \033[1;35mPAPEL\033[m')
print('\033[1;36m[ 2 ]\033[m - \033[1;36mTESOURA\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Escolha sua Jogada \033[1;31m[ 0 ]\033[m \033[1;35m[ 1 ]\033[m ou \033[1;36m[ 2 ]\033[m: '))
print('\033[4;32mJO\033[m')
sleep(0.5)
print('\033[4;32mKEN\033[m')
sleep(0.5)
print('\033[4;32mPÔ!!!\033[m')
sleep(0.5)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu')
    else:
        print('Computador Venceu')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    else:
        print('Jogador Venceu')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    else:
        print('Empate')
