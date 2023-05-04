#Ej 1

def fibonacci():
    a = 1
    b = 1
    contador = 0
    for i in range(0,40):
        c = a+b
        if i >= 12 and i <= 30:
            if c % 3 == 0:
                contador += 1
                print("El numero",c,"es multiplo de 3 y su posicion es", i)
        a,b=b,c
    print("Hay",contador,"numeros multiplos a 3")        
fibonacci()
