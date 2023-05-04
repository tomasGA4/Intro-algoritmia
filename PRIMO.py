#NUMERO PRIMO

def primo():
    nro = int(input("Ingrese un número: "))
    div = 1
    contdiv = 0
    while div <= nro:
        if nro % div == 0:
            contdiv = contdiv + 1
        div = div + 1
    if contdiv <= 2:
        print("Es un número primo")
    else:
        print("No es un número primo")
primo()


