from turtle import *
from random import *
# Turtle_Files
pantalla = Screen()
tortuga = Turtle()
DIM_X = 400
DIM_Y = 400
pantalla.setup(DIM_X + 25, DIM_Y + 25)
pantalla.screensize(DIM_X, DIM_Y)
tortuga.pensize(3)

# Variables
cont_pasos = 0
max_pasos = int(input("Cuantos pasos maximos quieres que de el pirata: "))
max_circulo = int(input("Cuan de grande quieres que sea el circulo de borracho: "))
# Programa
while cont_pasos < max_pasos:
    n = int(input("Cuantos pasos quieres que de el pirata: "))
    while n > 0:
        tortuga.forward(20)
        n -= 1
        cont_pasos += 1
        tortuga.circle(randint(0, max_circulo))
exitonclick()
