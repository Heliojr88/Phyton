# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto

pd = float(input('Digite o valor do produto: R$'))
vl = 5 * (pd/100)
vf = pd - vl
print('O valor com 5% de desconto é R${:.2f} e o novo valor do produto é R${:.2f}'.format(vl,vf))
