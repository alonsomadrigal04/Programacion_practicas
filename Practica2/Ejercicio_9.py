from turtle import *
from random import *

# Tortuga_file
pantalla = Screen()
DIM_X = 400
DIM_Y = 400
pantalla.setup(DIM_X + 25, DIM_Y + 25)
pantalla.screensize(DIM_X, DIM_Y)
tortuga = Turtle()
tortuga.speed(3)
# Programa
n = int(input("Dime el numero de trazos que deben haber: "))
otra = True
while otra:
    for i in range(n):
        redvar = random()
        greenvar = random()
        bluevar = random()
        tortuga.pensize(randint(0,20))
        tortuga.pencolor(redvar, greenvar, bluevar)
        tortuga.goto((randint(-DIM_X//2, DIM_X//2)), (randint(-DIM_Y//2, DIM_Y//2)))
    res = input("Quieres que vuelva ha dibujar una pasada, escribe s para si y cualquier otra cosa para no: ")
    if res != "s":
        otra = False