import pandas as pd
import matplotlib.pyplot as plt

#cargamos los datos mediante la ruta y read_csv:
ruta = 'Data_DeportistasBeneficiadosPAD_0_0.csv'
data_analizar = pd.read_csv(ruta, delimiter=';')

#convertimos la columna PAD a una cetgoria, y reemplazamos por mayusculas i y ii
data_analizar['PAD'] = data_analizar['PAD'].str.upper()

#agrupamos por tipo de PAD
monto_por_pad = data_analizar.groupby('PAD')['MONTO'].sum()

#creamos el grafico:
plt.figure(figsize=(10,6))
plt.bar(monto_por_pad.index, monto_por_pad.values, color='pink')
plt.title('Distribución del Monto total de apoyo por tipo de PAD')
plt.xlabel('Tipo de Pad')
plt.ylabel('Monto de apoyo (Soles)')
plt.tight_layout()
plt.show()