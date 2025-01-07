import numpy as np
mar = np.array ([
            [False,False,False,False,False],
            [False,False,False,False,False],
            [False,False,False,False,False],
            [False,False,False,False,False],
            [False,False,False,False,False]])

class Barco:
    def __init__(self, name):
        self.name = name
        self.ataques = 2

    def posicion(self, pos1, pos2):
        pos1=[]
        pos2=[]
    

class Jugador:
    def __init__(self, name):
        self.name= name

    def atacar(self, ataque):
        self.ataque= ataque
        ataque = []

    def colocar_barcos(self, pos1, pos2):
        Barco.posicion(self, pos1, pos2)

class Plataforma:
    def __init__(self):
        self.jugadores=[]
        self.barcos=[]

    def mostrar_mar():
        for false in mar:
        print("Mar")

    def enviar_ataques():
        pass
