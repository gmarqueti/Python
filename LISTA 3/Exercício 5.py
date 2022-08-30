#escreva um programa que leia um conjunto de inteiros e, em seguida, imprima a soma dos
#inteiros pares e ímpares

a=0
b=0
for x in range(0,15):
    n = int(input('Escreva números 15 numeros: '))
    if n % 2 == 0:
        a+=n
    else:
        b+=n
print('A soma dos pares foi: ', a)
print('A soma dos impares foi: ', b)
