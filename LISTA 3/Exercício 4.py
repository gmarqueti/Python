 #Escrever um algoritmo que leia uma quantidade números inseridos pelo usuário e conte quantos
#deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
#terminar quando for lido um número negativo.

n=1
C1=-0
C2=-0
C3=-0
C4=-0
while n > 0:
    n= int(input('Entre com um numero: '))
    if n >= 0 and n <= 25:
        C1 = C1 + 1
    elif n >= 26 and n <= 50:
        C2 = C2 + 1
    elif n >= 51 and n <= 75:
        C3 = C3 + 1
    elif n >= 76 and n <= 100:
        C4 = C4 + 1
    elif n < 0:
        print('Número inválido')
print('A quantidade de números entre 0 e 25 é = ', C1)
print('A quantidade de números entre 26 e 50 é =', C2 )
print('A quantidade de números entre 51 e 75 é = ', C3)
print('A quantidade de números entre 76 e 100 é = ', C4)