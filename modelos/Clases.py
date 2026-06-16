from dataclasses import dataclass,field

@dataclass
class Jugador: 
    nombre: str
    posicion: str
    edad: int
    
@dataclass
class Seleccion:
    nombre: str
    jugadores: list = field(default_factory=list)
    def agregar_jugador(self, jugador: Jugador):
        self.jugadores.append(jugador)
