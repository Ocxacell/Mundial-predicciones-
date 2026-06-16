import pandas as pd

#paso 1: Descubrir las selecciones y los jugadores por cada seleccion 

def extraer_csv(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
