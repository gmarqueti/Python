#Escreva um programa para encontrar o valor fatorialde um número ndigitado pelo usuário.
# O fatorial de um número n é da forma n! = n* (n -1) * (n -2) * ... * 2* 1Exemplo: 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

n= int(input("Escreva um número para calculo fatorial:"))
fat=1
cont=1

while cont <= n:
    fat = fat * cont
    cont = cont + 1

print(n ,"!=", fat)










