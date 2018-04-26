# Desenvolva o programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros dessa progressão.
print('='* 15)
print('10 TERMOS DE UMA PA')
print('=' * 15)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
total = primeiro + (10 - 1) * razão
for c in range(primeiro, total + razão, razão):
    print('{}'.format(c), end=' ')
print('Acabou')
