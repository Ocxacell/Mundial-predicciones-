from dataclasses import dataclass,field

@dataclass
class Seleccion:
    nombre: str
    jugadores: list = field(default_factory=list)

@dataclass
class Jugador: 
    nombre: str
    posicion: str
    edad: int
    