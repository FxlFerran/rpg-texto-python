import json
P = "python/"
#Jugador esta dividido por diccionarios: stats,equipo,inventario
#para facilitar la busqueda de cualquier cosa o la introduccion de esta
class Jugador():
    def __init__(self):
        with open(P + "estadisticas.json", "r") as f:
            self.todobtw = json.load(f)
    def recibir_dano(self,cantidad):
        self.vida -= cantidad-self.defensa
    def atacar(self,Enemigo):
        Enemigo.recibir_dano(self.daño)
    def inventario(self):
        for key in self.todobtw["inventario"]:
            print(str(self.todobtw["inventario"][key]["nombre"]) + " = " + str(self.todobtw["inventario"][key]))
    def recojer(self,drop):
        for obj in drop:
            temp = str(obj["nombre"]) + str(len(self.todobtw["inventario"]))
            self.todobtw["inventario"][temp] = obj
    def guardar(self):
        with open(P + "estadisticas.json", "w") as f:
            json.dump(self.todobtw, f, indent=4)
    def pruebas(self):
        print("Tu equipo actualmente es este:")
        for key in self.todobtw["equipo"]:
            if self.todobtw["equipo"][key] == "None":
                print(key+ " : " + str(self.todobtw["equipo"][key]))
            else:
                print(key+ " : " + str(self.todobtw["equipo"][key]["nombre"]))

drop = [{"nombre" : "pocion", "cura" : 15}, {"nombre" : 300}, {"nombre" : "pocion", "cura" : 30}]

jugador = Jugador()
jugador.guardar()
jugador.recojer(drop)
jugador.inventario()
