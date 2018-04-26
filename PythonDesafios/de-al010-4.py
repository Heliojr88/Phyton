# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas
vi = float(input('Digite a distância em km da sua viagem:  '))
if vi <= 200:
    pre = vi * 0.50
    print('O valor a ser cobrado é de R${:.2f} por {:.2f}km'.format(pre, vi))
else:
    pre = vi * 0.45
    print('O valor a ser cobrado é de R${:.2f} por {:.2f}km'.format(pre, vi))
