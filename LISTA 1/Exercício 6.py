# 6. Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
salário= float(input(" Entre com o salário: "))
imposto = salário >1200
print("Você deve pagar imposto ", imposto)