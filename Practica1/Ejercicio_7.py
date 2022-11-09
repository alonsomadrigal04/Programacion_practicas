# pantalla para turtle
from turtle import *
from math import sqrt

# Se pedirá el lado del cuadrado
lado = int(input("Dame el lado del cuadrado: "))

# Creación del Turtle
pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 400)
tortuga = Turtle()
tortuga.pensize(2)

# Dibujar cuadrado y la x
tortuga.write("(0, 0)")
tortuga.goto(lado, 0)
tortuga.goto(lado, lado)
tortuga.goto(0, lado)
tortuga.goto(0, 0)
tortuga.goto(lado,lado)
tortuga.goto(0, 0)
tortuga.goto(lado, 0)
tortuga.goto(0, lado)

# tejado
tortuga.left(45)
tortuga.forward(sqrt((lado**2)+(lado**2))/2)
tortuga.right(90)
tortuga.forward(sqrt((lado**2)+(lado**2))/2)

pantalla.exitonclick()