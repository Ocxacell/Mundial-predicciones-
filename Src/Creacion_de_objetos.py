from Modelos.Clases import Seleccion
from Modelos.Clases import Jugador

def crear_selecciones(df):
    selecciones = {}
    for nombre in df["Team"].unique():
        selecciones[nombre] = Seleccion(nombre)
    return selecciones

def crear_jugadores(df, selecciones):
    for _,row in df.iterrows():
        jugador =  Jugador(nombre=row['Player Name'], posicion=row['Position'], edad=row['Age'])
        selecciones[row['Team']].agregar_jugador(jugador)
    return selecciones