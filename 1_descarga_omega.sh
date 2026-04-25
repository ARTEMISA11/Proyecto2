#!/bin/bash

echo "Iniciando descarga de datos de Gaia DR3 para Omega Centauri..."

# La consulta ADQL con las coordenadas y el radio de 0.5 grados
QUERY="SELECT Source, RA_ICRS, DE_ICRS, pmRA, pmDE, Gmag, BPmag, RPmag FROM \"I/355/gaiadr3\" WHERE 1=CONTAINS(POINT('ICRS',RA_ICRS,DE_ICRS),CIRCLE('ICRS',201.691,-47.476,0.5))"

# Reemplazamos los espacios por '+' para que la URL sea válida
URL_QUERY=$(echo $QUERY | sed 's/ /+/g')
TAP_URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

# Ejecutamos wget hacia el servidor TAP
wget -q -O  omega_bruto.csv "$TAP_URL$URL_QUERY"

echo "Descarga completada: omega_bruto.csv" 

echo "Paso 2: Limpiando datos y creando base de datos SQL..."
python3 2_crear_db.py

echo "Paso 3: Generando análisis y gráficas..."
python3 3_analisis.py

echo "Proceso terminado exitosamente. Abriendo resultados..."
open grafica1.png grafica2.png
