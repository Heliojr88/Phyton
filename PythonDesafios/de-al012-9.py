# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% e juros
produto = float(input('Digite o valor do produto: '))
pagamento = str(input('Escolha a forma de pagamento ( Dinheiro, Cheque ou Cartão ) >>  ')).strip().upper()
if pagamento == 'DINHEIRO' or pagamento == 'CHEQUE':
    desconto = produto - (produto * 10 / 100)
    print('desconto de 10% R${:.2f}'.format(desconto))
elif pagamento == 'CARTÃO':
    cartao = str(input('a vista ou a prazo: ')).upper()
    if cartao == 'A VISTA':
        desconto = produto - (produto * 5 / 100)
        print('Desconto de 5% R$ {:.2f}'.format(desconto))
    elif cartao == 'A PRAZO':
        prazo = int(input('Quantas vezes: '))
        if prazo == 2:
            print('Sem Desconto R$ {:.2f}'.format(produto))
        else:
            juros = produto + (produto * 20 / 100)
            print('Acrescimo de 20% R$ {:.2f}'.format(juros))
else:
    print('Erro na digitação, tente novamente')
print('Obrigado')
