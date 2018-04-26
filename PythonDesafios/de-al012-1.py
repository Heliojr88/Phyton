# Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado
print('\033[31m =-=\033[m' * 8)
print('\033[4;32m Sistema de emprestimos EMPRA+\033[m')
print('\033[31m =-=\033[m' * 8)
nome = str(input('Qual seu nome: ')).strip().upper()
salario = float(input('Qual seu salário: '))
casa = float(input('Qual o valor da casa: '))
ano_pagamento = int(input('Quantos anos para pagar: '))
prestacao = casa / (ano_pagamento * 12)
mes = ano_pagamento * 12
if prestacao >= (salario * 30 / 100):
    print('Infelizmente seu emprestimo foi \033[1;31mNEGADO\033[m tente novamente daqui a 6 anos')
else:
    print('Sr. \033[33m{}\033[m, seu emprestimo foi autorizado!!'.format(nome))
    print('Valor da casa de R$ \033[31m{:.2f}\033[m'.format(casa))
    print('Valor da prestação mensal sem juros \033[36mR$ {:.2f}\033[m'.format(prestacao))
    print('Total ser pago é de {} anos ou {} mês'.format(ano_pagamento, mes))
print('\033[31m =-=\033[m' * 10)
print('\033[30m O banco \033[m\033[7;31;40mEMPRA+\033[m \033[30magradece a preferência\033[m')
print('\033[31m =-=\033[m' * 10)
