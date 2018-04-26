# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
totmaior = 0
tomenor = 0
for p in range(1, 8):
    nasc = int(input('Em que ano nasceu a {} pessoa: '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        tomenor += 1
print('Ao todo tivemos {} pessoa maiores de idade'.format(tomenor))
print('Ao todo tivemos {} pessoas de menor idade'.format(tomenor))