#Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade
#expressa em dias. Considere um ano = 365 dias e um mês = 30 dias.
def função(n1, n2, n3,):
    dias = n1*365 + n2*30 * n3
    print('Você tem {} dias vividos'.format(dias))

n1 = int(input('Qual sua idade? '))
n2 = int(input('Quantos meses ? '))
n3 = int(input('E quantos dias? '))

função(n1, n2, n3)