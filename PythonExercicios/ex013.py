# Faça um  algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

vs = float(input('Digite seu salário: R$'))
pg = vs + (vs*15/100)
print('Seu aumento de 15% é R${:.2f} e o seu novo salário é R${:.2f}'.format(vs*15/100, pg))