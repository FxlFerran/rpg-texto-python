import os
def Color(color, texto):
    colores = {
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m",
        "reset": "\033[0m"
    }
    
    return f"{colores.get(color, '')}{texto}{colores['reset']}"

def pelea():
    pass

def Bucle():
    while 1 > 0:
        sel = input(
"""\n1.Iniciar Incursion
2.Tienda
3.Entrenamiento
4.Salir y Guardar\n""")
        os.system("cls" if os.name == "nt" else "clear")

        match sel:
            case "1":
                inc = input(
f"""\n
                            Antes de entrar en la {Color("rojo","MAZMORRA")} se recomienda prepararse con equipo
                            1.Entrar a la {Color("rojo","MAZMORRA")} con {Color("azul","EQUIPO ACTUAL")}
                            2.Cambiar {Color("azul","EQUIPO")} {Color("verde","(armas,pociones y otros)")}
                            """)
                match inc:
                    case "1":
                        pass

                    case "2":
                        print(
f"""\n                          {Color("rojo","MIEDICA")}, pero bueno te entiendo es algo {Color("rojo","muuuuyyyyy dificil")}, {Color("azul","tu inventario")};
                              {Color("verde","para seleccionar cosas tendras que elegir su numero y decir que si esto hara que se cambie con el objeto que tengas: (espada1) -> (espada2)")}""")
            case "2":
                print(
f"""\n                      Cada vez que salgas de una {Color("rojo","MAZMORRA")} la tienda se {Color("azul","REINICIARA")} con diferentes {Color("verde","OBJETOS ACORDE A TU NIVEL")}\n""")
            case "3":
                print(
f"""\n
                               Al entrenar {Color('azul','te cansaras')} pero te haras {Color('rojo','MAS FUERTE!')}
                      {Color('verde','''***AL CANSARTE TENDRAS UN DEBUFF AL ENTRAR EN LA MAZMORRA O ENTRENARTE,
                         PUEDES RECUPERARTE CON POCIONES O AL MORIR:''')} {Color('rojo','(pierdes dinero)***')}\n""")
            case "4":
                ("Guardando y Saliendo...")
                break
            case _:
                print(f"""Recuerda que tienes que elegir un numero de los que hay ahi si no no podras jugar y eso es {Color("rojo","MALO")}""")

Bucle()
