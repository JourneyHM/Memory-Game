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
tapCount = 0    # Contador de taps
duoCount = 0    # Contador de parejas que se van generando



# Definición de medidas de cada cuadrado del juego

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

# Pasar de coordenadas a valores en la lista de tiles

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Pasar de valores en la lista de tiles a coordenadas x, y

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200



def tap(x, y):
    """Update mark and hidden tiles based on tap."""

    global tapCount
    tapCount += 1
    spot = index(x, y)
    mark = state['mark']
  

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
    

    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global duoCount
        duoCount += 1           # Se anexa un contador de parejas encontradas
       
    

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

    if duoCount == 1:
        up()
        goto(0,-235)  
        color('black')
        write('YOU WIN :D', font=('Arial', 25, 'normal'), align = 'center')         # Al ganar se despliega el mensaje "YOU WIN :D", aunque para hacer pruebas con una pareja encontrada lo ejecuta
    
    
    up()
    goto(-70,210)  
    color('black')
    write('Taps:', font=('Arial', 10, 'normal'), align = 'center')      # Visualización de texto "Taps" para dar a entender que se cuentan los taps que el jugador va haciendo

    up()
    goto(-45,210)  
    color('black')
    write(tapCount, font=('Arial', 10, 'normal'), align = 'center')    # Despliegue de contador de taps

    up()
    goto(75,210)  
    color('black')
    write(duoCount, font=('Arial', 10, 'normal'), align = 'center')    # Despliegue de contador de parejas formadas

    up()
    goto(25,210)  
    color('black')
    write('Couples found:', font=('Arial', 10, 'normal'), align = 'center')    # Despliegue de texto "Couples found" para dar a entender que se cuentan las parejas encontradas al momento
    
    
    
    

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(500, 500, 370, 0)   # Medidas especializadas del despliegue de turtle
addshape(car)
hideturtle()
tracer(False)

onscreenclick(tap)
draw()
done()
