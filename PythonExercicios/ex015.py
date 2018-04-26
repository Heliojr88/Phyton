# Escreva um programa que pergunte a quantidade de km percorridos por im carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado

d = int(input('Quantos dias ficou com o carro: '))
km = float(input('Quantos km foram rodados: '))
pg = (d*60)+(km*0.15)
print('O valor total a ser pago é de R$ {:.2f}'.format(pg))