# Faça um  algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

vs = float(input('Digite seu salário: '))
pg = 15 * (vs/100)
vn = vs + pg
print('Seu aumento de 15% é R${} e o seu novo salário é R${}'.format(pg, vn))