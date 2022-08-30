# 10. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias=int(input("Informe o número de dias: "))
horas= int(input("Informe o númedo de horas: "))
minutos=int(input("Informe o número de minutos: "))
segundos= float(input("Informe o número de segundos: "))
dseg= dias*86400
hseg= horas*3600
mseg=minutos*60
segtotal= dseg+hseg+mseg+segundos
print("O total de Segundos é: ", segtotal)