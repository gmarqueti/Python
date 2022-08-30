#Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10.
# Use o formato de apresentação (considerando que o usuário informouo número 5):
# 5 x 1 = 55 x 2 = 105 x 3 = 15etc...
n= int (input("Escreva o número:"))
seq = 0
tab = 0
while seq <= 9:
    seq += 1
    tab= tab + n
    print (n ,"*" ,seq ,"=" , tab )


