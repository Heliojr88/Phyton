# faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input('Digite um ano: '))
bi = ano % 4
res = bi
#res2 = ano % 100
if res == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))