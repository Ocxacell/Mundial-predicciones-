from Modelos.Clases import Seleccion
from Modelos.Clases import Jugador

def crear_selecciones(df):
    selecciones = {}
    for nombre in df["Team"].unique():
        selecciones[nombre] = Seleccion(nombre)
    return selecciones