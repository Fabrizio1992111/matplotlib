# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

# Especificar el directorio donde están los archivos
#os.chdir("/home/fabrizio/Escritorio/TUBO/")

# Cargar los datos de los archivos
data1 = np.loadtxt('/home/fabrizio/Escritorio/TUBO/IRR_GROWTH_gr1.OUT', skiprows=1)
data2 = np.loadtxt('/home/fabrizio/Escritorio/VPSCIRR/VP-SA/STR_STR100.OUT', skiprows=1, usecols=(2, 3, 4))
data3 = np.loadtxt('/home/fabrizio/Escritorio/TUBO/STRAIN113CORR1-100MPA.txt', skiprows=6, usecols=(10, 11, 12))
data4 = np.loadtxt('/home/fabrizio/Escritorio/TUBO/STRAIN113CORR2-100MPA.txt', skiprows=6, usecols=(10, 11, 12))


data5 = np.loadtxt('/home/fabrizio/Escritorio/VPSCIRR/VP-SA/STR_STR200.OUT', skiprows=1, usecols=(2, 3, 4))
data6 = np.loadtxt('/home/fabrizio/Escritorio/TUBO/STRAIN113CORR2-200MPA.txt', skiprows=6, usecols=(10, 11, 12))
data7 = np.loadtxt('/home/fabrizio/Escritorio/TUBO/STRAIN113CORR1-200MPA.txt', skiprows=6, usecols=(10, 11, 12))
#data4 = np.loadtxt('STR_STR(ensayo3).OUT', skiprows=1, usecols=(2, 3, 4))

# Crear listas para almacenar los datos
x1 = data1[:, 0]
y2 = data2[:, 2]
y3 = data3[:, 2]
y4 = data4[:, 2]
y5 = data5[:, 2]
y6 = data6[:, 2]
y7 = data7[:, 2]

# Graficar los datos
fig, ax = plt.subplots()
ax.plot(x1, y2, color='r', label='VPSC-SA-100 MPA',linewidth=2)
ax.plot(x1, y3, color='b', label='CORROT-100 MPA',linewidth=2)
ax.plot(x1, y4, color='g', label='TEXROT-100 MPA',linewidth=2)
ax.plot(x1, y5, color='r', linestyle='--' ,label='VPSC-SA-200 MPA',linewidth=2)
ax.plot(x1, y6, color='g', linestyle='--' ,label='TEXROT-200 MPA',linewidth=2)
ax.plot(x1, y7, color='b', linestyle='--' ,label='CORROT-200 MPA',linewidth=2)

# Agregar etiquetas a los ejes
ax.set_xlabel('Dosis (DPA)')
ax.set_ylabel('Growth Strain')

# Establecer los límites en x
ax.set_xlim(0, 5)
# Establecer los límites en y
ax.set_ylim(0, 1.5e-02)

# Agregar título al gráfico
#ax.set_title('VPSC-SA-r')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()


