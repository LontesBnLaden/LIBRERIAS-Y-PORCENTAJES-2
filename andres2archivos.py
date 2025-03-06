import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x
x = np.linspace(0, 2 * np.pi, 100)  # 100 puntos entre 0 y 2π

# Calcular los valores de seno y coseno
seno = np.sin(x)
coseno = np.cos(x)

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(x, seno, color='red', label='Seno')
plt.plot(x, coseno, color='blue', label='Coseno')

# Añadir título y etiquetas
plt.title('Funciones Seno y Coseno')
plt.xlabel('x (radianes)')
plt.ylabel('Valor')
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Línea horizontal en y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Línea vertical en x=0
plt.grid()
plt.legend()
plt.show()