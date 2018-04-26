# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    maioridade = atual - ano
    if maioridade >= 18:
        cont += 1
    elif maioridade < 18:
        cont1 += 1
print('{} já são maiores de idade e {} ainda não são maiores de idade'.format(cont, cont1))
