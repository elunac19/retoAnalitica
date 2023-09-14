import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("openpowerlifting.csv")

# Al correr el codigo muestra la primera gráfica que es un 
# subplot de boxplots sobre los comparativos de edad y peso 
# de carga de cada tipo de ejercicio


#Aqui tuve que poner abs value, debido a que algunos values dan negativos pero es por error de sistema de obtencion de datos. 
df['BestSquatKg'] = df['BestSquatKg'].abs()
df['BestBenchKg'] = df['BestBenchKg'].abs()
df['BestDeadliftKg'] = df['BestDeadliftKg'].abs()

df['Age_Group'] = pd.cut(df['Age'], bins=range(0, 101, 10), right=False, labels=range(0, 100, 10))

# Crear un subplot de boxplots ------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
# Primer subplot: BestBenchKg vs. Age_Group
sns.boxplot(data=df, x='Age_Group', y='BestBenchKg', ax=axes[0])
axes[0].set_title('Comparación - Age vs. BestBenchKg')
axes[0].set_xlabel('Age Group')
axes[0].set_ylabel('BestBenchKg')
# Segundo subplot: BestSquatKg vs. Age_Group
sns.boxplot(data=df, x='Age_Group', y='BestSquatKg', ax=axes[1])
axes[1].set_title('Comparación - Age vs. BestSquatKg')
axes[1].set_xlabel('Age Group')
axes[1].set_ylabel('BestSquatKg')
# Tercer subplot: BestDeadliftKg vs. Age_Group
sns.boxplot(data=df, x='Age_Group', y='BestDeadliftKg', ax=axes[2])
axes[2].set_title('Comparación - Age vs. BestDeadliftKg')
axes[2].set_xlabel('Age Group')
axes[2].set_ylabel('BestDeadliftKg')
plt.tight_layout()
plt.show()

# Crear un mapa de calor ---------------------------------------------------------
plt.figure(figsize=(10, 8))
corr = df.corr(numeric_only = True)
sns.heatmap(data = corr, annot=True, cmap='YlOrRd', fmt=".2f", linewidths=0.5)
plt.title('Mapa de Calor de Correlación entre Variables')
plt.show()

# Crear un subplot de histogramas ------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
# Primer subplot: Histograma de Peso vs. BestBenchKg
sns.histplot(data=df, x='BodyweightKg', y='BestBenchKg', ax=axes[0], bins=20)
axes[0].set_title('Histograma - Peso vs. BestBenchKg')
axes[0].set_xlabel('Peso')
axes[0].set_ylabel('BestBenchKg')
# Segundo subplot: Histograma de Peso vs. BestSquatKg
sns.histplot(data=df, x='BodyweightKg', y='BestSquatKg', ax=axes[1], bins=20)
axes[1].set_title('Histograma - Peso vs. BestSquatKg')
axes[1].set_xlabel('Peso')
axes[1].set_ylabel('BestSquatKg')
# Tercer subplot: Histograma de Peso vs. BestDeadliftKg
sns.histplot(data=df, x='BodyweightKg', y='BestDeadliftKg', ax=axes[2], bins=20)
axes[2].set_title('Histograma - Peso vs. BestDeadliftKg')
axes[2].set_xlabel('Peso')
axes[2].set_ylabel('BestDeadliftKg')
plt.tight_layout()
plt.show()
