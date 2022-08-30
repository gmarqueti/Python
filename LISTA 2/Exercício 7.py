#7. Faça um programa que dados três valores X, Y e Z, verifica se eles podem ser os comprimentos
#dos lados de um triângulo e, se forem, verificar se é um triângulo equilátero, isósceles ou escaleno.
#Caso eles não formem um triângulo, escreva uma mensagem.
#• Para verificar se as três medidas formam um triângulo, cada soma entre as medidas de
#dois lados deve ser maior que a terceiro lado.
#o Lado A + Lado B > Lado C
#o Lado A + Lado C > Lado B
#o Lado B + Lado C > Lado A
x=float(input("Escreva o 1° valor: "))
y=float(input("Escreva o 2° valor: "))
z=float(input("Escreva o 3° valor: "))

if x + y <= z and x + z <= y and y + z <= x:
    print('Não é um triângulo')
else:
    print('É um Triângulo')
