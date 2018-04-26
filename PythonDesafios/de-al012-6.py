# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
from datetime import date
data = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - data
if idade <= 9:
    print('MIRIM')
    print('Sua idade é %s' % idade)
elif 10 <= idade <= 18:
    print('INFANTIL')
    print('Sua idade é %s anos' % idade)
elif idade == 19:
    print('JUNIOR')
    print('Sua idade é %s anos' % idade)
elif idade == 25:
    print('SÊNIOR')
    print('Sua idade é %s anos' % idade)
else:
    print('MASTER')
    print('Sua idade é %s anos' % idade)
print('Obrigado')
