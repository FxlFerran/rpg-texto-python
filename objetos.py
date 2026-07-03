import json,os
#nombre, calidad, tipo, daño/cura
#tipo = normal,fuego,hielo,tierra,aire,celestial,demoniaco

# Division del objeto al ser una clase: 
# dentro del objeto tendra 4
# 1. El nombre lo mas importante del objeto para poder saber cual es
# 2. las estadisticas: daño extra, si añade defensa o cura
# 3. el valor, lo divido para facilitar el verlo
# 4. EFECTO, no lo mas importante del objeto si es que este no tiene efecto
# la idea del EFECTO es que literalmente seria un codigo directo metido a este
# habrian varios objetos con el mismo EFECTO porque si no mucho codigo XD

class creacion():
    def __init__(self):
        daño,defensa,cura= 0,0,0
        self.nombre = input("Dale un nombre al objeto: ")
        Pstats = input("elige entre los numeros, puedes elegir uno o varios (tambien todos): 1.daño 2.defensa 3.cura 4.efecto: ")
        for x in Pstats:
            match x:
                case "1":
                    daño = int(input("daño: "))
                case "2":
                    defensa = int(input("defensa: "))
                case "3":
                    cura = int(input("cura: "))
                case "4":
                    self.efecto = input("daño: ")
        self.stats = [daño,defensa,cura]

espada_de_dios = creacion()

x = 0
while x != "*":


    with open("objetos.json", "r") as f:
        lst_obj = json.load(f)
        lst_obj[objeto-1][cld-1].append(x) 
    with open("objetos.json", "w") as f:
        json.dump(lst_obj,f , indent=4)
    x = input("Salir: *: ")
    os.system("clear")


