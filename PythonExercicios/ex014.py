# Conversões de temperaturas C° F° K°

c = float(input('Digite qual a temperatura atual em celsius: '))
f = (1.8*c) + 32
k = c + 273
print('A temperatura em Farenheit é {:.2f}°F e em Kelvin é {:.2f}°K'.format(f, k))