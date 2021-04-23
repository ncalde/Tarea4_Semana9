#Este código corresponde al método de diferencias finitas utilizando un número de iteraciones como criterio de parada.

#Se importan las librerías que se consideran necesarias
import numpy as np
import matplotlib.pyplot as plt

def aproxTemp (totalpuntos,totaltiempo,alfa,Txy,iter):
    """
          Esta función se encarga de ejecutar el método de diferencias finitas.

          El ciclo seguirá iterando hasta realizar la cantidad de iteraciones deseadas..

          totalpuntos: cantidad de puntos a evaluar en la coordenada espacial.
          totaltiempo: cantidad de puntos a evaluar en la coordenada temporal.
          alfa: constante del problema necesaria para resolver la ecuación diferencial.
          Txy: matriz de puntos sobre la que se va a trabajar.
          iter: número de iteraciones al realizar

       """
    contador_iteraciones = 0 #Variable que lleva un registro de número de iteraciones.

    # El ciclo for recorre la matriz y calcula la solución para cada punto.

    while contador_iteraciones < iter:
        contador_iteraciones = contador_iteraciones+1
        for m in range (0, totaltiempo-1):
            for n in range (1, totalpuntos-1):
                Txy[m+1,n] = (alfa)*(Txy[m,n+1]-2*Txy[m,n]+Txy[m,n-1])+Txy[m,n]
    valorTemp = Txy
    return valorTemp

totalpuntos = 50
# constante necesarias para resolver el problema
totaltiempo = 500
longitud = 10
segundos = 10
A = 2.0
D = 0.5
x0 = 5.0
dt = segundos/(totaltiempo-1) #Espaciado entre los puntos en x
dx = longitud/(totalpuntos-1) #Espaciado entre los puntos en t
alfa = dt*D/dx**2
iter = 300 # Número de iteraciones a realizar

#se crea el espacio sobre el que se va a calcular la EDP
x = np.linspace(0,longitud,totalpuntos)
y = np.linspace(0,segundos,totaltiempo)
X, Y = np.meshgrid(x,y)

def matrizInicial (totalpuntos,totaltiempo, A, x0,x):
    """
            Se crea la matriz que representa el espacio sobre el que se va a calcular la EDP
        """
    Txy = np.zeros((totaltiempo,totalpuntos))
    for i in range (1,totalpuntos-1):
        Txy[0,i] = A*np.exp(-((x[i]-x0)**2)/1.5)
    return Txy

#Se llama a la función que crea la matriz Txy
Matriz = matrizInicial(totalpuntos,totaltiempo,A,x0,x)

#Se llama a la función que soluciona la EDP
Temperatura = aproxTemp(totalpuntos,totaltiempo,alfa,Matriz,iter)

#Se grafican los resultados
plt.figure(figsize=(10, 6))
ax = plt.axes(projection='3d')
ax.set_xlabel('x (m)')
ax.set_ylabel('t (s)')
ax.set_zlabel('T (Celsius)')
ax.plot_surface(X, Y, Temperatura, rstride=1, cstride=1,
                cmap='plasma', edgecolor='none')
ax.set_title('Difusión de calor')
plt.show()