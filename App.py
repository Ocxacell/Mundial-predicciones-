import pandas as pd
from Src.Extraccion_de_datos import extraer_csv, extraer_selecciones_jugadores
from Src.Creacion_de_objetos import crear_selecciones
from Src.Creacion_de_objetos import crear_jugadores
from Src.Transformaciones_de_datos import NacimientoAedad

from Modelos.Clases import Seleccion
#Paso 1: Extraer daots

df_selecciones = extraer_csv('Data/SquadLists.csv')
df_selecciones = NacimientoAedad(df_selecciones)
df_selecciones.head()
Selecciones = crear_selecciones(df_selecciones)
Selecciones = crear_jugadores(df_selecciones, Selecciones)
print(Selecciones['Mexico'].jugadores[0])


#Crear objeto seleccion y jugador 
