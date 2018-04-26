# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
sal = float(input('Digite seu salário: R$'))
if sal >= 1250.00:
    aum = (sal * 10 / 100) + sal
    print('O aumento de seu salário sera de 10% e o seu novo salário é de R${:.2f}'.format(aum))
else:
    aum2 = (sal * 15 / 100) + sal
    print('O aumento de seu salário será de 15% e seu novo salário é de R${:.2f}'.format(aum2))
print('A empresa agradece sua colaboração')