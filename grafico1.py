import pandas as pd
import matplotlib.pyplot as plt

#cargamos los datos:
data = 'Data_DeportistasBeneficiadosPAD_0_0.csv'
data_depor = pd.read_csv(data, delimiter=';')

#agrupamos los datos para graficar apoyo por año
monto_por_anio = data_depor.groupby('ANIO')['MONTO'].sum()

#ahora creamos el grafico:
plt.figure(figsize=(10, 6))
plt.bar(monto_por_anio.index, monto_por_anio.values, color= 'skyblue')
plt.title('Distribución del Monto de Apoyo por Año')
plt.xlabel('Año')
plt.ylabel('Monto de Apoyo (SOLES)')
plt.xticks(rotation=45)
plt.tight_layout #parq que entre todo en el grafico y no se salga nada
plt.show()
