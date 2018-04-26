# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto

pd = float(input('Digite o valor do produto: R$'))
vl = pd - (pd*5/100)
print('O total com 5% de desconto é R${:.2f} e o novo valor do produto é R${:.2f}'.format(pd*5/100, vl))