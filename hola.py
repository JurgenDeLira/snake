import turtle

class Scrfeen:
    def __init__(self, ancho, alto, titulo, fondo):
        self.ancho = ancho
        self.ventana = turtle.Screen()
        self.ventana.title(titulo)
        self.ventana.bgcolor(fondo)
        self.ventana.setup(width=ancho, height= alto)
        self.ventana.tracer(0)
        canvas = self.ventana.getcanvas()
        root =   canvas.winfo_toplevel()  
        root.protocol("WM_DELETE_WINDOW",self.on_close)
    def on_close(self):
        print("cerrado")
        self.ventana.bye()
    def setArena(self,lado, colorBorde, cuadricula = False):
        self.lado = lado
        self.colorBorde = colorBorde

        if cuadricula:
            ver = turtle.Turtle()
            #hor = turtle.Turtle()
            ver.speed(0)
            #hor.speed(0)

            #ver.hideturtle()
            ver.goto(-self.lado/2, -self.lado/2)
            self.ventana.update()


ventana = Scrfeen(600, 600, "Snake", "white")
ventana.setArena(400, "red", True)


ventana.ancho

turtle.mainloop()