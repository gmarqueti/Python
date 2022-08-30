#4. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
#resultado da operação solicitada
a= float(input(" Escreva o primeiro número: "))
b= float(input("Escreva o segundo número: "))
operacao= input( "Qual operação?")
if operacao == '+' :
    conta=(a+b)
    print(conta)
elif operacao == "-":
    conta= (a-b)
    print (conta)
elif operacao == "*":
    conta= (a*b)
    print (conta)
elif operacao == "/":
    conta= (a/b)
    print (conta)
else:

    print ("Operação não realizada")