from turtle import *

# Entradas
peldanos = int(input("dime el numero de peldaños: "))
long = int(input("Dime la logitud de los mismos: "))

# Tortuga_files
pantalla = Screen()
DIM_X = 400
DIM_Y = 400
tortuga = Turtle()
tortuga.pensize(2)
pantalla.setup(DIM_X+25, DIM_Y+25)
pantalla.screensize(DIM_X, DIM_Y)

# Creación de la escalera
tortuga.forward(long*peldanos)
tortuga.left(90)
for i in range(peldanos):
    tortuga.forward(long)
    tortuga.left(90)
    tortuga.forward(long)
    tortuga.right(90)
tortuga.left(180)
tortuga.forward(long*peldanos)
exitonclick()