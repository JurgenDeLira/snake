from ScrfeenClass import Scrfeen
from ComidaClass import Comida
from SerpienteClass import Serpiente
from SerpienteClass import Game
import time



juego = Game(0.2)
juego.puntaje("white")

ventana = Scrfeen(600, 600, "Snake", "black")
ventana.setArena(400, "red", False)

snake = Serpiente("white","gray")
snake.controles(ventana.ventana, "Up","Down", "Left", "Right")

comida = Comida("red", ventana)

while juego.running:
    ventana.ventana.update()
    if juego.perder:
        juego.alPerder(snake, ventana, comida)
    if comida.alColisionar(snake, juego):
        comida.alColisionar(snake,juego)
        snake.moverCuerpo()
        continue
    snake.moverCuerpo()
    snake.movimiento(juego, ventana)
    snake.colision(snake,juego, ventana, comida)
    time.sleep(juego.delay)

