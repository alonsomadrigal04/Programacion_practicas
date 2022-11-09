from turtle import *

# Pedir medidas

lados = int(input("Dame la longitud del lado: "))
while lados < 0:
    lados = int(input("El lado tiene que ser > 0: "))
vert = int(input("Dame ahora el número de vertices: "))
while vert < 0:
    vert = int(input("Los vertices han de ser > 0: "))
rad = int(input("Dame el radio de los circulos que decorarán las figuras: "))
while rad <0:
    rad = int(input("El radio no puede ser negativo: "))

# Spawnear la tortuga
pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 400)
tortuga = Turtle()
tortuga.pensize(2)

# Dibujar figura
for i in range(vert):
    for a in range(4):
        tortuga.forward(lados/4)
        tortuga.circle(-rad)

    tortuga.left(180-((vert-2)*180/vert))

exitonclick()
