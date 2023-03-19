import os
import sys

def calculo_media(numeros):
    soma = sum(numeros)
    u = soma/len(numeros)
    return u


def calculo_desvios(numeros, u):
    lista_desvios = []
    for numero in numeros:
        lista_desvios.append((numero-u)**2)
    return lista_desvios


def variancia_desvio(us):
    return round(us**(1/2), 3)


def input_dado(numeros):
    try:
        numeros.append(float(input("numero: ")))
        os.system('clear')
        return numeros
    except ValueError:
        os.system('clear')
        print("\n\n\n--> somante numeros <--\n\n\n")

    

def main():
    os.system('clear')
    numeros = []
    lista_desvios = []
    print("numeros",numeros)
    #return
    while True:
        # os.system('clear')
        numeros = input_dado(numeros)

        u = calculo_media(numeros)
        print("Numeros", numeros)
        print("Média: ", u)
        lista_desvios = calculo_desvios(numeros, u)

        print("Desvio pradrão-> ", lista_desvios)
        print('{}'.format(variancia_desvio(calculo_media(lista_desvios))))


# try:
#     numeros = sys.argv[1]
# except IndexError:
#     numeros = False

main()
