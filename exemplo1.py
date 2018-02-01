import math

def newton_method(m,x):

    for i in range(1,m+1):
        #newX = x - (pow(x,3) - 2 * x - 5)/(3 * pow(x,2) - 2)
        #newX = x - (pow(x, 6) - 2) / (6 * pow(x, 5))
        #newX = x - ((math.cos(x) - x)/(-math.sin(x) - 1))

        #Exemplo a
        #newX = x - (pow(x, 3) - 30)/(3 * pow(x, 2))

        #Exemplo b
        #newX = x - (pow(x, 7) - 1000)/(7 * pow(x, 6))

        #Exemplo c
        #newX = x - (pow(x, 13) - 13)/(13 * pow(x, 12))

        newX = x - (2 * pow(x, 3) - 6 * pow(x, 2) + 3 * x + 1) / (6 * pow(x, 2) - 12 * x + 3)

        x = newX

        print("X %d = %.6f"%(i, newX))


newton_method(15, 2)