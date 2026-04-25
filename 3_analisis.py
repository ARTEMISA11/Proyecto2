import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos
conexion= sqlite3.connect('arqueologia.db')

# GRÁFICA 1: Movimiento Propio  
df_todas = pd.read_sql_query("SELECT * FROM estrellas", conexion)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

#plt.figure(figsize=(8, 6))
ax1.scatter(df_todas['pmRA'], df_todas['pmDE'], s=0.5, alpha=0.3, color='gray')
ax1.set_title('Movimiento Propio: Vía Láctea vs Omega Centauri')
ax1.set_xlabel('RA (mas/yr)')
ax1.set_ylabel('DEC (mas/yr)')
ax1.set_xlim(-15, 10)
ax1.set_ylim(-15, 10)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.scatter(df_todas['pmRA'], df_todas['pmDE'], s=0.5, alpha=0.3, color='gray')
ax2.set_title('Zoom al cumulo')
ax2.set_xlabel('RA (mas/yr)') 
ax2.set_ylabel('DEC (mas/yr)')
ax2.set_xlim(-8, 2)
ax2.set_ylim(-11, -1)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.savefig('grafica1.png', dpi=300)
print("Gráfica 1 guardada.")

# GRÁFICA 2: Diagrama Color-Magnitud
consulta= "SELECT * FROM estrellas WHERE pmRA BETWEEN -5.0 AND -1.0 AND pmDE BETWEEN -9.0 AND -5.0"
df_omega = pd.read_sql_query(consulta, conexion)

df_omega['Color_BP_RP'] = df_omega['BPmag'] - df_omega['RPmag']
df_omega['M_Gmag'] = df_omega['Gmag'] - 13.7 

plt.figure(figsize=(6, 8))
plt.scatter(df_omega['Color_BP_RP'], df_omega['M_Gmag'], s=0.8, alpha=0.5, color='darkblue')
plt.gca().invert_yaxis() 
plt.title('Diagrama HR de Omega Centauri')
plt.xlabel(r'$B - R$')
plt.ylabel(r'$G_{mag}$ ABS')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('grafica2.png', dpi=300)
print("Gráfica 2 guardada.")

conexion.close()
