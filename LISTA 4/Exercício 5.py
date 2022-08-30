# Escreva um programa para calcular a soma dos números que aparecem em uma determinada
#string. Se não houver números, gere uma exceção dizendo que a string não contém números.
#A string fornecida é: 15 é25 uma 20string
numero = ''
soma = 0
frase = input('Digite uma frase contendo números: ')
for n in frase:
    if n.isnumeric():
        numero += n
    elif numero != '':
        soma += int(numero)
        numero = ''
if numero != '':
    soma += int(numero)
    print('a soma é:', soma)
elif soma == 0:
    print('não contém números')
