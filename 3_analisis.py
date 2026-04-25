import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos
conexion= sqlite3.connect('arqueologia.db')

# GRÁFICA 1: Movimiento Propio  
df_todas = pd.read_sql_query("SELECT * FROM estrellas", conexion)

plt.figure(figsize=(8, 6))
plt.scatter(df_todas['pmRA'], df_todas['pmDE'], s=0.5, alpha=0.3, color='gray')
plt.title('Movimiento Propio: Vía Láctea vs Omega Centauri')
plt.xlabel('pmRA (mas/yr)')
plt.ylabel('pmDE (mas/yr)')
plt.xlim(-15, 10)
plt.ylim(-15, 10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('grafica1.png', dpi=300)
print("Gráfica 1 guardada.")

# GRÁFICA 2: Diagrama Color-Magnitud
consulta= "SELECT * FROM estrellas WHERE pmRA BETWEEN -5.5 AND 0.0 AND pmDE BETWEEN -8.5 AND -4.0"
df_omega = pd.read_sql_query(consulta, conexion)

df_omega['Color_BP_RP'] = df_omega['BPmag'] - df_omega['RPmag']
df_omega['M_Gmag'] = df_omega['Gmag'] - 13.7 

plt.figure(figsize=(6, 8))
plt.scatter(df_omega['Color_BP_RP'], df_omega['Gmag'], s=0.8, alpha=0.5, color='darkblue')
plt.gca().invert_yaxis() 
plt.title('Diagrama HR de Omega Centauri')
plt.xlabel(r'$BP - RP$')
plt.ylabel(r'$G_{mag}$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('grafica2.png', dpi=300)
print("Gráfica 2 guardada.")

conexion.close()
