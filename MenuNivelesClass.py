import turtle
from ScrfeenClass import Scrfeen

class MenuNiveles:

    def __init__(self, scrfeen,backMethod, initGameMethod):
        self.pantalla = scrfeen.ventana
        self.screen = scrfeen

        self.noveles = ["Fácil", "Normal", "Dificil"]

        self.opcion_seleccionada = None
        self.nivel_actual = 0

        self.backMethod = backMethod
        self.initGameMethod = initGameMethod

        self.titulo = turtle.Turtle()
        self.titulo.speed(0)
        self.titulo.color("white")
        self.titulo.penup()
        self.titulo.goto(0,250)

        self.titulo.write("Menú niveles", align = "center", font = ("Courier",36, "bold"))
        self.titulo.hideturtle()


        self.texto_nivel = turtle.Turtle()
        self.texto_nivel.speed(0)
        self.texto_nivel.color("white")
        self.texto_nivel.penup()
        self.texto_nivel.goto(0,210)

        self.texto_nivel.write("Selecciona el nivel del juego", align = "center", font = ("Courier",24, "normal"))
        self.texto_nivel.hideturtle()
        self.agregar_boton_atras()
        turtle.mainloop()
    def agregar_boton_atras(self):
        boton_atras = turtle.Turtle()
        boton_atras.speed(0)
        boton_atras.color("white")
        boton_atras.penup()
        boton_atras.goto(-260,260)
        boton_atras.write("<", align= "center", font = ("Courier",24, "normal") )
        boton_atras.hideturtle()


def initGame():
    print("init")

def backMethod():
    print("back")
ventana = Scrfeen(600, 600, "Juego de Snake", "black")
menu = MenuNiveles(ventana,backMethod, initGame)

       