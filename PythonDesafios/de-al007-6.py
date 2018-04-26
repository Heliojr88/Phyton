# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere U$ 1,00 = R$ 3,27

dh = float(input('Digite quanto dinheiro tem na carteira: '))
cv = dh / 3.33
print('Com R${} você pode comprar U${:.3} dolares'.format(dh,cv))