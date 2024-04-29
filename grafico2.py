import pandas as pd
import matplotlib.pyplot as plt

#cargamos los datos:
ruta = 'Data_DeportistasBeneficiadosPAD_0_0.csv'
data = pd.read_csv(ruta, delimiter=';') #en un block de notas sacamos el delimitador

#Agrupamos los datos para ver el numero de deportias apoyados por año:
deportistas_por_anio = data.groupby('ANIO')['ITEM'].nunique()

#creamos el grafico:
plt.figure(figsize=(10,6))
plt.bar(deportistas_por_anio.index, deportistas_por_anio.values, color='lightgreen')
plt.title('Número de Deportistas apoyados por año')
plt.xlabel('Año')
plt.ylabel('Número de Deportistas')
plt.tight_layout()
plt.show()

