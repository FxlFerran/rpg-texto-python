import random,json
P = "python/"

class Tienda():
    def __init__(self):
        self.lst_obj = []
        self.obj1 = None
        with open(P + "objetos.json", "r") as f:
            objetos = json.load(f)
        self.lst_obj.append(objetos)
    def seleccion(self):
        #Armadura,herramientas,objetos/Calidad/objeto
        #[0,1,2]/[0,1,2,3]/[0,1,2,...,x]
        #self.lst_obj[0][2][0][0]
        for i in range(6):
            y = random.randrange(len(self.lst_obj[0]))
            x = random.randrange(len(self.lst_obj[0][y][0]))
            for i in range(1):
                       print(self.lst_obj[0][y][0][x])

    def caracteristicas(self,obj):
        if "dano" in obj:
            x = "dano"
            z = f"\ntipo: {obj['tipo']}"
        elif "cura" in obj:
            x = "cura"
            z = ""
        else:
            x = "defensa"
            z = f"\ntipo: {obj['tipo']}"
        print(f"CARACTERISTICAS DEL OBJETO:\nNombre: {obj['nombre']}\nCalidad: {obj['calidad']}{z}\n{x}: {obj[x]}")

tienda = Tienda()
tienda.seleccion()

