import turtle

class Scrfeen():

    def __init__(self, ancho, alto, titulo, fondo):
        self.ventana = turtle.Screen()
        self.ventana.title(titulo)
        self.ventana.bgcolor(fondo)
        self.ventana.setup(width=ancho, height=alto)
        self.ventana.tracer(0)

        # Configuro boton de cerrar
        canvas = self.ventana.getcanvas()
        root = canvas.winfo_toplevel()

        def on_close():
            print("cerrado")
            self.ventana.bye()

        root.protocol("WM_DELETE_WINDOW", on_close)

    # Método para el espacio de juego
    def setArena(self, lado, colorBorde, cuadricula=False):
        self.lado = lado
        self.colorBorde = colorBorde

        # Configuración de la Cuadricula si se desea mostrar, por defecto es False
        if cuadricula:
            ver = turtle.Turtle()
            ver.speed(5)
            ver.hideturtle()
            ver.goto(-(self.lado/2)-10, -(self.lado/2)-10)
            ver.color("white")
            ver.left(90)
            for i in range(10):
                ver.forward(self.lado)
                ver.right(90)
                ver.forward(20)
                ver.right(90)
                ver.forward(self.lado)
                ver.left(90)
                ver.forward(20)
                ver.left(90)

            hor = turtle.Turtle()
            hor.speed(5)
            hor.hideturtle()
            hor.goto(-(self.lado/2)-10, -(self.lado/2)-10)
            hor.color("white")
            for i in range(10):
                hor.forward(self.lado)
                hor.left(90)
                hor.forward(20)
                hor.left(90)
                hor.forward(self.lado)
                hor.right(90)
                hor.forward(20)
                hor.right(90)

        arena = turtle.Turtle()
        arena.speed(1)
        arena.hideturtle()
        arena.goto(-(self.lado/2)-10, -(self.lado/2)-10)
        arena.color(colorBorde)
        for i in range(4):
            arena.forward(self.lado)
            arena.left(90)
        self.ventana.update()



