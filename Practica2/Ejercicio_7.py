from turtle import *

# Entradas
dist = int(input("Dame la distancia de cada tortuga: "))
ang = int(input("Dame el angulo inicial: "))

# Tortuga_Files
pantalla = Screen()
DIM_X = 400
DIM_Y = 400
pantalla.setup(DIM_X + 25, DIM_Y + 25)
pantalla.screensize(DIM_X, DIM_Y)
tortuga = Turtle()
tortuga.pensize(2)
tortuga.shape("turtle")
tortuga.penup()

# Programa
while tortuga.xcor() < abs(DIM_X//2) and tortuga.ycor() < abs(DIM_Y//2):
    tortuga.stamp()
    tortuga.forward(dist)
    tortuga.right(ang)
    dist += 2
exitonclick()
