# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = date.today().year
#nome = str(input('Qual seu nome: ')).strip()
data = int(input('Digite seu ano de nascimento: '))
idade = ano - data
alistamento = 18
if idade == 18:
    print('Está no ano para o alistamento')
elif idade < 18:
    falta = alistamento - idade
    print('Ainda não está no ano para o alistamento, faltam {} anos'.format(falta))
else:
    acima = idade - alistamento
    print('Você ja passou {} anos para se alistar'.format(acima))
