from turtle import *
from random import *

# Entradas
n = int(input("Dime los trazos que deben haber: "))

# Tortuga_file
pantalla = Screen()
DIM_X = 400
DIM_Y = 400
pantalla.setup(DIM_X + 25, DIM_Y + 25)
pantalla.screensize(DIM_X, DIM_Y)
tortuga = Turtle()


# Programa
for i in range(n):
    redvar = random()
    greenvar = random()
    bluevar = random()
    tortuga.pensize(randint(0,20))
    tortuga.pencolor(redvar, greenvar, bluevar)
    tortuga.goto((randint(-DIM_X//2, DIM_X//2)), (randint(-DIM_Y//2, DIM_Y//2)))
exitonclick()