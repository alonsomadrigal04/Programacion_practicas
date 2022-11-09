# Imports
from turtle import *
from math import *
# Entradas

lado = int(input("Dame el lado de un cuadrado, y lo inscribiré en un circulo: "))
hip = sqrt((lado**2)+(lado**2))
coord_x = int(input("ahora dame las coordenadas de un punto deseado, coordenada x: "))
coord_y = int(input("Ahora la coordenada y: "))

# Creación del Turtle
pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 400)
tortuga = Turtle()
tortuga.pensize(2)

# Cuadrado
tortuga.write("({0}, {1})".format(0, 0))
tortuga.penup()
tortuga.goto(0, -lado/2)
tortuga.pendown()
tortuga.pencolor("red")
tortuga.forward(lado/2)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado/2)

# circulo

tortuga.pencolor("blue")
tortuga.penup()
tortuga.goto(0, -hip/2)
tortuga.pendown()
tortuga.circle(hip/2)

# Punto

if -lado/2 < coord_x < lado/2 and -lado/2 < coord_y < lado/2:  # Comprobamos el valor que las coord. están dentro del cuadrado
    tortuga.penup()
    tortuga.goto(coord_x, coord_y)
    tortuga.pencolor("red")
    tortuga.pendown()
    tortuga.dot()
elif abs(coord_x) > abs(hip / 2) or abs(coord_y) > abs(hip / 2):  # comprobamos que al menos una coord. esta más allá de las dos figuras
    tortuga.penup()
    tortuga.goto(coord_x, coord_y)
    tortuga.pencolor("green")
    tortuga.pendown()
    tortuga.dot()
else:   # si ninguna se cumple estará entre el circulo y el cuadrado
    tortuga.penup()
    tortuga.goto(coord_x, coord_y)
    tortuga.pencolor("blue1")
    tortuga.pendown()
    tortuga.dot()

pantalla.exitonclick()
