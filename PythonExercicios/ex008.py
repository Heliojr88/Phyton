# Escreva um programa que leia um valor em metro e o exiba convertido em centímetros e milimetros
m = float(input('Digite um valor em metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
milha = m * 0.000621371
jr = m * 1.09361
pe = m * 3.28084
pol = m * 39.3701
mn = m * 0.000539957
print('O valor digitado em quilômetro é {}km \nhectômetro é {}hm \ndecâmetro {}dam \ndecímetro {}dm \ncentímetro {}cm \nmilímetro {}mm \nmilhas {} \njarda {} \npé {} \npolegadas {} \nmilha nautíca {}'.format(km, hm, dam, dm, cm, mm, milha, jr, pe, pol, mn))
