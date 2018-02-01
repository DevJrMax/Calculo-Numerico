import matplotlib.pyplot as plt

eixoX = []
eixoM = []

def newtonMethod(inicio, fim, passo, casas):

    while(inicio!=fim):
        x=inicio
        x = x - (2 * pow(x,3) - 6 * pow(x, 2) + 3 * x + 1) / (6 * pow(x,2) - 12 * x + 3)
        print("Inicio",inicio,"=",round(x/passo,casas))
        eixoX.append(inicio)
        eixoM.append(x)
        inicio = inicio + 0.01
        inicio = round(inicio, 2)


newtonMethod(2.0,3.0,1000,6)

plt.plot(eixoX, eixoM, 'bo')
plt.show()