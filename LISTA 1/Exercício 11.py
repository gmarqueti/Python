# 11. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a  percorrer e a velocidade média esperada para a viagem
distancia= float(input("Informe a distância que será percorrida em metros/seg: "))
velocidade= float(input("Informe a velocidade média do percurso em metros/seg: "))
tempo= distancia/velocidade
print ("O tempo estimado é de ", tempo, "segundos")