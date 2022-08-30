#3. Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
# salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
#15%.
sal= float(input("Informe seu salário: "))
if sal<= 1250:
    aumento= ((sal/100)*15)
    SalTot= (sal+aumento)
elif sal>1250:
    aumento= ((sal/100)*10)
    SalTot=(sal+aumento)
print("Seu salário com o aumento é: R$",SalTot)