# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu sataus, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite se peso: (Kg) '))
imc = peso / (altura * altura)
if imc <= 16:
    print('Magreza grave')
    print('Seu índice é de {:.2f}'.format(imc))
elif 16.1 <= imc <= 17:
    print('Magreza moderada')
    print('Seu índice é de {:.2f}'.format(imc))
elif 17.1 <= imc <= 18.5:
    print('Magreza leve')
    print('Seu índice é de {:.2f}'.format(imc))
elif 18.6 <= imc <= 25:
    print('Saudável')
    print('Seu índice é de {:.2f}'.format(imc))
elif 25.1 <= imc <= 30:
    print('Sobrepeso')
    print('Seu índice é de {:.2f}'.format(imc))
elif 30.1 <= imc <= 35:
    print('Obesidade grau I')
    print('Seu índice é de {:.2f}'.format(imc))
elif 35.1 <= imc <= 40:
    print('Obesidade grau II(SEVERA)')
    print('Seu índice é de {:.2f}'.format(imc))
else:
    print('Obesidade grau III (MÓRBIDA)')
    print('Seu índice é de {:.2f}'.format(imc))
print('Obrigado')