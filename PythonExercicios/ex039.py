# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = date.today().year
sexo = str(input('Qual seu sexo: [ F ] [ M ] ')).upper()
if sexo == 'M':
    data = int(input('Digite o ano de nascimento: '))
    idade = ano - data
    print('Quem nasceu em {} tem {} anos em {}'.format(data, idade, ano))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        falta = ano + saldo
        print('Seu alistamento será em {} ano'.format(falta))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        falta = ano - saldo
        print('Seu alistamento foi em {}'.format(falta))
else:
    print('Você não precisa se alistar')