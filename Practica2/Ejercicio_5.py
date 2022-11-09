from turtle import *

# Entradas
r = int(input("Dime el radio de una circunferencia: "))
n = int(input("Dime el numero de puntos random que quieres que ponga: "))
count = 0
# Tortuga_files
tortuga = Turtle()
tortuga.pensize(2)
pantalla = Screen()
DIM_X = 400
DIM_Y = 400
pantalla.setup(DIM_X+25, DIM_Y+25)
pantalla.screensize(DIM_X, DIM_Y)

# Dibujar el ciculo
tortuga.penup()
tortuga.right(90)
tortuga.forward(r)
tortuga.pendown()
tortuga.left(90)
tortuga.circle(r)

# puntos
for i in range(n):
    tortuga.penup()
    coord_x = int(input("Dame una coord x: "))
    coord_y = int(input("Dame una coord y: "))
    tortuga.goto(coord_x, coord_y)
    tortuga.dot()
    if abs(coord_x) < r and abs(coord_y) < r:
        count += 1

print("Hay {0} puntos dentro del cuadrado".format(count))

exitonclick()