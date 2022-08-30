#5. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para
#indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
kw= float(input("Digite a quantidade de Kwh consumida:"))
tpi= input("Informe o tipo de instalação, sendo: R para residências, I para indústrias e C para comércios:")
if tpi == "r":
    if kw <= 500:
        conta= kw*0.40
        print("O valor a se pagar é:R$", conta)
    else:
        conta= kw*0.65
        print("O valor a se pagar é:R$", conta)
if tpi=="c":
    if kw <= 1000:
        conta= kw*0.55
        print("O valor a se pagar é:R$", conta)
    else:
        conta= kw*0.60
        print("O valor a se pagar é:R$", conta)
if tpi=="i":
    if kw<= 5000:
        conta= kw*0.55
        print("O valor a se pagar é:R$", conta)
    else:
        conta = kw*0.60
        print("O valor a se pagar é:R$", conta)