import os


def calculo_media(numeros):
    soma = sum(numeros)
    u = soma/len(numeros)
    return u


def main():
    os.system('clear')
    numeros = []
    lista_devios = []
    while True:
        try:
            numeros.append(float(input("numero: ")))
            os.system('clear')
            u = calculo_media(numeros)
            print("Numeros", numeros)
            print("Média: ", u)
            lista_devios = []
            for numero in numeros:
                lista_devios.append((numero-u)**2)

            print("Desvio pradrão-> ", lista_devios)

            us = calculo_media(lista_devios)

            print(round(us**(1/2), 2))
        except ValueError:
            os.system('clear')
            print("somante numeros")


main()
