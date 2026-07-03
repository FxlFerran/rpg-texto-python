class Enemigo():
    def __init__(self):
        self.vida = 30
        self.defensa = 5
        self.def_esp = 10
        self.daño = 15
    def recibir_dano(self,cantidad):
        self.vida -= cantidad-self.defensa
    def atacar(self,Jugador):
        Jugador.recibir_dano(self.daño)


