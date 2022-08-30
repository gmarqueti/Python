#Construa um algoritmo que, dado o primeiro elemento a1 e a razão r de uma progressão
#aritmética (PA), imprima todos os n primeiros elementos da PA, onde a1, r e n são informados
#pelo usuário. Lembre-se que uma PA pode ser crescente ou decrescente.
a1= int(input("Escreva o primeiro elemento:"))
r= int(input("Informe a razão da p.a:"))
n=int(input("Infome até quando vai a p.a:"))
n=n+1

for cont in range (a1,r,n):
    print(cont, end = " ")

