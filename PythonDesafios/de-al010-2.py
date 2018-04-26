# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite
km = float(input('Digite a velocidade: '))
if km <= 80.00:
    print('Não foi Multado')
    print('Parabéns você está no limite da via que é de 80km')
else:
    multa = (km - 80) * 7
    print('Você foi Multado e o valor a ser pago é de R$ {:.2f}'.format(multa))
    print('Dirija com mais cuidado')
print('O DETRAN agradece')