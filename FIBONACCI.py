#FIBONACCI

def fibonacci():
    a = 1
    b = 1
    for i in range(0,50):
        c = a+b
        print(c, end=" ")
        a,b=b,c
fibonacci()