# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem n final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a nota de português: '))
n2 = float(input('Digite a nota de matemática: '))
media = (n1 + n2) / 2
print(media)
if media <= 5:
    print('REPROVADO')
elif 5.1 <= media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
