# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere U$ 1,00 = R$ 3,27

dh = float(input('Digite quanto dinheiro tem na carteira: R$ '))
cv = dh / 3.34
print('Com R${:.2f} você pode comprar US${:.2f} dolares'.format(dh,cv))