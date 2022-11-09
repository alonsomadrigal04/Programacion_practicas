# pantalla para turtle
from turtle import *

# Se pedirá el lado del cuadrado
coord_x = int(input("Dame las coorednadas del centro del círculo en (primero la x): "))
coord_y = int(input("Ahora la y: "))
rad = int(input("Dame el radio del círculo en cuestión: "))

# Creación del Turtle
pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 400)
tortuga = Turtle()
tortuga.pensize(2)

# dibujar circulo
tortuga.penup()
tortuga.goto(coord_x, coord_y)
tortuga.pendown()
tortuga.write("({0}, {1})".format(coord_x, coord_y))
tortuga.penup()
tortuga.goto(coord_x, -rad)
tortuga.pendown()
tortuga.circle(rad)
tortuga.up()
tortuga.goto(coord_x, coord_y)
tortuga.pendown()
tortuga.forward(rad)
tortuga.write("Radio: ¨{0}". format(rad))
pantalla.exitonclick()
