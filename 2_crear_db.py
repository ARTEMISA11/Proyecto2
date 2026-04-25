import pandas as pd
import sqlite3

print("Leyendo archivo CSV...")
# 1. Leer el archivo CSV
df = pd.read_csv('omega_bruto.csv')

# 2. Limpiar valores nulos en cinemática y fotometría
columnas_clave = ['pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag']
clean_df = df.dropna(subset=columnas_clave)

print(f"Datos originales: {len(df)}. Datos limpios: {len(clean_df)}.")

# 3. Crear base de datos local y conectar
conexion = sqlite3.connect('arqueologia.db')

# 4. Transferir el DataFrame a una tabla SQL llamada 'estrellas'
clean_df.to_sql('estrellas', conexion, if_exists='replace', index=False)
print("Datos migrados a Arqueologia.db en la tabla estrellas")
conexion.close()
print("Base de datos 'arqueologia.db' creada exitosamente.")
