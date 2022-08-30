# 2. Escreva um programa que leia três números e que imprima o maior e o menor
a= float(input("Escreva o primeiro número: "))
b= float(input("Escreva o segundo número: "))
c= float(input("Escreva o terceiro número: "))
if (a>b) and (a>c) and (c>b):
    print("Maior:" ,a ,"Menor: " ,b)
elif (b>a) and (b>c) and (c>a):
    print("Maior: ", b, "Menor: ", a)
elif (c>a) and (c>b) and (a>b):
    print("Maior: ", c, "Menor: ", b)
elif (b>a) and (b>c) and (a>c):
    print("Maior", b, "Menor:", c)
elif (a>b) and (a>c) and (b>c):
    print("Maior: ", a, "Menor: ", c)
elif (c>a) and (c>b) and (b>a):
    print ("Maior: ", c, "Menor: ", a)