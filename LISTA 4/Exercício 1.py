#Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume
#v = 4/3 x PI x R³, com PI = 3,14
def volume(r):
    vol = 4/3 * 3.14 * r**3
    print('O volume da esfera é {:.2f}'.format(vol))

r = float(input('Digite o valor do raio da esfera: '))
volume(r)
