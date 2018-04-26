# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu sataus, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Seu peso: (Kg) '))
altura = float(input('Sua altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Normal')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em obesidade morbida')