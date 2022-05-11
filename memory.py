"""
Juego: De Memoria


Programador 1: Ivan Santiago Hernandez Mendoza - A01662556
Programador 2: Diego Jacobo Martínez - A01656583  

Fecha: 11 / 05 / 2022

"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tapCount = 0



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""

    global tapCount
    tapCount+= 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)  # Haciendo referencia a la línea 31, en donde se hacen cuadros con una distancia de 50 en cada lado, es por eso qeu usamos x + 25
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align = 'center')    # Agregamos un " align = center", para centrar el texto de tiles.    

    up()
    goto(-20,210)  
    color('black')
    write('Taps:', font=('Arial', 10, 'normal'), align = 'center')      # Código correspondiente a texto en la parte de arriba del juego, señalizando Taps

    up()
    goto(0,210)  
    color('black')
    write(tapCount, font=('Arial', 10, 'normal'), align = 'center')    # Despliegue de contador de taps
    
    

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)

onscreenclick(tap)
draw()
done()
