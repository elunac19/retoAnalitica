import numpy as np
import pandas as pd

df = pd.read_csv("openpowerlifting.csv")

#Aqui tuve que poner abs value, debido a que algunos values dan negativos pero es por error de sistema de obtencion de datos. 
df['BestSquatKg'] = df['BestSquatKg'].abs()
df['BestBenchKg'] = df['BestBenchKg'].abs()
df['BestDeadliftKg'] = df['BestDeadliftKg'].abs()

columns_describe = ['Sex','Equipment','Age','BodyweightKg','WeightClassKg','BestSquatKg','BestBenchKg','BestDeadliftKg']

#Aquí se puede ver una breve representación de los datos obtenidos.
print( df.head() )

#Aquí se pueden apreciar más claramente el tipo de variables que se encuentran en los datos.
print( df.info() )

# Este comando es para imprimir la información general sobre los datos, como el promedio, max, min, 
# la diferencia de valores entre las variables (std) y el número de valores contados.
print( df[columns_describe].describe() )

#CONCLUSIÓN ---
#Valores como min y max, no se relacionana con ninguna de las otras variables, pues simplemente cuentan el max o min valor
#una variable. Sin embargo, si tomas encuenta el mean de todas las variables puedes darte una idea general de los powerlifters.
