# pantalla para turtle
from turtle import *

# Se pedirá el lado del cuadrado
lado = int(input("Dame el lado del cuadrado: "))

# Creación del Turtle
pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 400)
tortuga = Turtle()

tortuga.pensize(2)

# Dibujar
tortuga.write("(0, 0)")
tortuga.goto(lado, 0)
tortuga.write("({0}, 0)".format(lado))
tortuga.goto(lado, lado)
tortuga.write("({0}, {0})".format(lado))
tortuga.goto(0, lado)
tortuga.write("(0, {0})".format(lado))
tortuga.goto(0, 0)
pantalla.exitonclick()