import turtle
from ScrfeenClass import Scrfeen
class Serpiente:
    def __init__(self, colorCabeza, colorSegmento):
        self.segmentos = []
        self.cabeza = turtle.Turtle()
        self.cabeza.speed(0)
        self.cabeza.shape("square")
        self.cabeza.color(colorCabeza)
        self.cabeza.penup()
        self.cabeza.goto(0,0)


        self.cabeza.direction = "stop"

        self.colorSegmento = colorSegmento

    def controles(self, ventana, arriba, abajo, izquierda, derecha):
        ventana.listen()
        ventana.onkeypress(self.arriba, arriba)
        ventana.onkeypress(self.abajo, abajo)
        ventana.onkeypress(self.izquierda, izquierda)
        ventana.onkeypress(self.derecha, derecha)

    def arriba(self):
        print("arriba")
        if self.cabeza.direction != "down":
            self.cabeza.direction = "up"
    def abajo(self):
        print("abajo")
        if self.cabeza.direction != "up":
            self.cabeza.direction = "down"
    
    def derecha(self):
        print("derecha")
        if self.cabeza.direction != "left":
            self.cabeza.direction = "right"
    
    def izquierda(self):
        print("izquierda")
        if self.cabeza.direction != "right":
            self.cabeza.direction = "left"

    def movimiento(self, screen):
        if self.cabeza.direction == "up":
            y = self.cabeza.ycor()
            if y < (screen.lado/2-20):
                self.cabeza.sety(y+20)
            else:
                print("se ha perdido el juego")
        if self.cabeza.direction == "down":
             y = self.cabeza.ycor()
             if y> -(screen.lado/2):
                 self.cabeza.sety(y-20)
             else:
                print("se ha perdido el juego")
        if self.cabeza.direction == "left":
            x = self.cabeza.xcor()
            if x> -(screen.lado/2):
                self.cabeza.setx(x-20)
            else:
                print("se ha perdido el juego")
        if self.cabeza.direction == "right":
            x = self.cabeza.xcor()
            if x<(screen.lado/2-20):
                self.cabeza.setx(x+20)
            else:
                print("se ha perdido el juego")  
    
    def agregarSegmentos(self):
        self.nuevo_segmento = turtle.Turtle()
        self.nuevo_segmento.speed(0)
        self.nuevo_segmento.shape("square")
        self.nuevo_segmento.color(self.colorSegmento)
        self.nuevo_segmento.penup()
        self.segmentos.append(self.nuevo_segmento)
    
    def moverCuerpo(self):
        tamanio = len(self.segmentos)
        for i in range(tamanio - 1, 0, -1):
            x = self.segmentos[i-1].xcor()
            y = self.segmentos[i-1].ycor()
            self.segmentos[i].goto(x,y)
        if tamanio > 0:
            x = self.cabeza.xcor()
            y = self.cabeza.ycor()
            self.segmentos[0].goto(x,y)
    
    def colision(self):
        for seg in self.segmentos:
            if seg.distance(self.cabeza) < 20:
                print("juego perdido")
