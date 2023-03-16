import os


def calculo_media(numeros):
    soma = sum(numeros)
    u = soma/len(numeros)
    return u


def main():
    os.system('clear')
    numeros = []
    lista_desvios = []
    while True:
        try:
            numeros.append(float(input("numero: ")))
            os.system('clear')
            u = calculo_media(numeros)
            print("Numeros", numeros)
            print("Média: ", u)
            lista_desvios = []
            for numero in numeros:
                lista_desvios.append((numero-u)**2)

            print("Desvio pradrão-> ", lista_desvios)

            us = calculo_media(lista_desvios)
            print(round(us**(1/2), 2))
        except ValueError:
            os.system('clear')
            print("somante numeros")


main()
