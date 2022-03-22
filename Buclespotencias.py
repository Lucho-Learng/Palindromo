# contador = 2
# print("4 elevado a la " + str(contador) + " es igual a: " + str(4**contador))


def run():
    LIMITE = 10000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a la " + str(contador) +
              " es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()
