#. O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de
#substituição na qual cada letra do texto e substituída por outra, que se apresenta no alfabeto abaixo
#dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituído
#por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente um programa que faça uso desse
#Código de César, entre com uma string e retorne a string codificada. Exemplo:
#String: a ligeira raposa marrom saltou sobre o cachorro cansado
#Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
text = input('Texto a ser criptografado: ').upper().replace(' ', '0')


def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


s = int(input('Chave: '))
print(encrypt(text, s).replace('f', ' '))
