# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% e juros
print('{:=^40}'.format(' LOJAS HJ '))
compras = float(input('Qual o valor das suas compras: R$ '))
print('''Qual a forma de pagamento: 
[ 1 ] - Dinheiro
[ 2 ] - Cheque
[ 3 ] - Cartão de débito
[ 4 ] - 2x no cartão de crédito
[ 5 ] - 3x ou mais no cartão de crédito''')
opção = int(input('Escolha a opção: '))
if opção == 1:
    total = compras - (compras * 10 / 100)
elif opção == 2:
    total = compras - (compras * 10 / 100)
elif opção == 3:
    total = compras - (compras * 5 / 100)
elif opção == 4:
    total = compras
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 5:
    total = compras + (compras * 20 /100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção inválida de pagamento. tente novamente')
print('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format(compras, total))
