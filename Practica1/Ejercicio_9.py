# tortuga
from turtle import *
# Entradas
lado = int(input("Dame el lado del cuadrado y te lod ibujaré además de su circulo inscrito: "))
# Creación del Turtle
pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 400)
tortuga = Turtle()
tortuga.pensize(2)

# dibujar circulo
tortuga.penup()
tortuga.goto(0, -lado)
tortuga.pendown()
tortuga.circle(lado/2)

# dibujar cuadrado
tortuga.forward(lado/2)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado/2)
pantalla.exitonclick()
