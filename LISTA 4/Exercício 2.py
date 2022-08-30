#Faça um procedimento que recebe a idade de um nadador e retorna, a categoria desse nadador
#de acordo com a tabela
def idade(i):
    if i >= 5 and i <=7:
        print('Infantil A')

    elif i >= 8 and i <=10:
        print('Infantil B')

    elif i >= 11 and i <= 13:
        print('Juvenil A')

    elif i >= 14 and i <= 17:
        print('Juvenil B')

    elif i >= 18:
        print('Adulto')



i = int(input('Qual sua idade: '))
idade(i)