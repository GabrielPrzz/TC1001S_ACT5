"""Memory puzzle game with colors and numbers."""
from random import *
from turtle import *
from freegames import path

car = path('car.gif')

# 32 colores diferentes (necesitamos 32 pares para 64 casillas)
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 
          'pink', 'cyan', 'magenta', 'brown', 'gold', 'lime',
          'turquoise', 'salmon', 'khaki', 'coral', 'teal', 'navy',
          'olive', 'maroon', 'tomato', 'skyblue', 'springgreen', 'violet',
          'indigo', 'aquamarine', 'peachpuff', 'wheat', 'tan', 'plum', 'orchid', 'darkseagreen']

# Crear 32 pares diferentes: [(color, número), ...] * 2
base_tiles = [(colors[i], i + 1) for i in range(32)]
tiles = base_tiles + base_tiles  # 64 elementos totales

state = {'mark': None}
hide = [True] * 64
tap_count = 0

def square(x, y, fill_color='white', number=None):
    """Draw square with color and number at (x, y)."""
    up()
    goto(x, y)
    down()
    pencolor('black')
    fillcolor(fill_color)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
    
    # Escribir número en el centro
    if number is not None:
        up()
        goto(x + 25, y + 15)
        color('white')
        write(number, align='center', font=('Arial', 28, 'bold'))

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count
    if all_revealed():
        return
    
    tap_count += 1
    spot = index(x, y)
    mark = state['mark']
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def all_revealed():
    """Return True if all tiles have been uncovered."""
    return not any(hide)

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    mark = state['mark']
    
    # Dibujar todos los cuadrados
    for count in range(64):
        x, y = xy(count)
        color_tile, num = tiles[count]
        
        if hide[count]:
            # Si está oculto pero es el marcado, mostrar color y número
            if count == mark:
                square(x, y, color_tile, num)
            else:
                # Si está oculto y no es marcado, blanco sin número
                square(x, y, 'white')
        else:
            # Si está revelado, mostrar color y número
            square(x, y, color_tile, num)
    
    # Mostrar contador de intentos
    up()
    goto(-195, 175)
    color('black')
    write(f'Intentos: {tap_count}', font=('Arial', 14, 'bold'))
    
    # Mensaje de victoria
    if all_revealed():
        up()
        goto(0, -220)
        color('red')
        write(f'¡Ganaste en {tap_count} intentos!', align='center', font=('Arial', 20, 'bold'))
    
    update()
    if not all_revealed():
        ontimer(draw, 100)

# Configurar y ejecutar
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
