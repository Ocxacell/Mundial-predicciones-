import pandas as pd
from Src.Extraccion_de_datos import extraer_csv, extraer_selecciones_jugadores
from Src.Creacion_de_objetos import crear_selecciones
from Modelos.Clases import Seleccion
#Paso 1: Extraer daots

df_selecciones = extraer_csv('Data/SquadLists.csv')

Selecciones = crear_selecciones(df_selecciones)
print(Selecciones['Mexico'])

jugadores_por_seleccion, selecciones = extraer_selecciones_jugadores(df_selecciones)

#Crear objeto seleccion y jugador 
