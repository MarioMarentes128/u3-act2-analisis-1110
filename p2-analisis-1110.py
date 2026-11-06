# importar librerias
import pandas as pd
import numpy as np
print("Analisis de datos empleados Mario Yañez NC=1110")

empleados = {
    "Empleado": ["Elena", "Sergio", "Lucia", "Gonzalo", "Valeria", "Diego"],
    "Departamento": ["Ventas", "IT", "HR", "IT", "Ventas", "Finanzas"],
    "Horas_Capacitacion": [40, 80, 25, 60, 90, 15],
    "Evaluacion_Desempeno": [8.5, 9.2, 7.0, 8.8, 9.6, 6.5]
}

df = pd.DataFrame(empleados)
print(df)
print("-+-+-+ Agrupar por una sola columna Departamento-+-+-+")
grouped = df.groupby('Departamento')
print(grouped)
print(" -+-+-+ por agregacion -+-+-+")
# horas-Capacitacion por Departamento
print(grouped['Horas_Capacitacion'].mean())

# evaluacion:desempeño de cada Empleado
print(grouped['Evaluacion_Desempeno'].max())