# Crie um programa que leia uma frase qualquer e diga se ela e um palíndromo, desconsiderando os espaços
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso2 = ''.join(palavras)[::-1]
vermelho = '\033[33m'
#inverso = junto[::-1] # com fatiamento
for letra in range(len(junto) - 1, -1, -1):
   inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso2))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo')

