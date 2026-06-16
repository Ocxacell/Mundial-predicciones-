import pandas as pd

#paso 1: Descubrir las selecciones y los jugadores por cada seleccion 

def extraer_csv(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    return df

def extraer_selecciones_jugadores(df):
    selecciones = df['Team'].unique()
    jugadores_por_seleccion = {}
    
    for seleccion in selecciones:
        jugadores = df[df['Team'] == seleccion]['Player Name'].tolist()
        jugadores_por_seleccion[seleccion] = jugadores
        
    return jugadores_por_seleccion,selecciones