# Memory 🧠

## Descripción

**Memory** es un clásico juego de puzzle de pares de números. Destapa losetas para encontrar los pares coincidentes. Mejora tu memoria mientras intentas emparejar todos los números en la menor cantidad de movimientos posible.

## Requisitos

- **Python** 3.7+
- **turtle** (incluido en la instalación estándar de Python)
- **freegames** (librería personalizada)

## Instalación

### 1. Clonar o descargar el repositorio
```bash
git clone https://github.com/tu-usuario/memory-game.git
cd memory-game
```

### 2. Instalar dependencias
```bash
pip install freegames
```

## Uso

Ejecuta el juego con:
```bash
python memory.py
```

## Cómo Jugar

🎮 **Objetivo:** Encontrar todos los pares de números iguales

📋 **Reglas:**
1. **Click en un loseta** para revelar un número
2. **Click en otra loseta** para intentar encontrar su pareja
3. Si los números coinciden → quedan revelados ✅
4. Si no coinciden → se ocultan nuevamente ❌
5. **Gana cuando todos los pares estén descubiertos** 🎉

## Características

✅ **Grid 8x8** - 64 losetas con 32 pares de números  
✅ **Sistema de memoria** - Rastrea números ocultos y revelados  
✅ **Interfaz intuitiva** - Simplemente haz click para jugar  
✅ **Animación suave** - Actualización cada 100ms  
✅ **Números aleatorios** - Orden diferente cada partida  

## Estructura del Código

```
memory.py
├── Variables Globales
│   ├── tiles       # Array con pares de números (32 números × 2)
│   ├── hide        # Array booleano que rastrea losetas ocultas
│   └── state       # Diccionario con 'mark' (primera selección)
├── Funciones Gráficas
│   ├── square()    # Dibuja un cuadrado de loseta
│   └── draw()      # Renderiza el juego
├── Lógica del Juego
│   ├── index()     # Convierte coordenadas (x,y) a índice
│   ├── xy()        # Convierte índice a coordenadas (x,y)
│   └── tap()       # Maneja clicks del ratón
└── Configuración
    └── setup(), onscreenclick(), done()
```

## Ejemplo de Partida

```
1. Haces click en loseta [0] → aparece "15"
2. Haces click en loseta [5] → aparece "8" (no coincide, se ocultan)
3. Haces click en loseta [12] → aparece "15" (coincide con [0]!)
4. Haces click en loseta [5] → aparece "8" (coincide con otra)
✅ Par encontrado!
5. Repites hasta encontrar todos los pares...
```

## Ejercicios de Mejora

El código incluye 5 ejercicios sugeridos:

### 1. Contar y imprimir taps 📊
```python
state = {'mark': None, 'taps': 0}

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    state['taps'] += 1
    print(f"Taps totales: {state['taps']}")
    
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
```

### 2. Reducir a grid 4x4 🎯
```python
# Cambiar de 8x8 (64 tiles) a 4x4 (16 tiles)
tiles = list(range(8)) * 2  # 8 números × 2 = 16 losetas
hide = [True] * 16

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)  # Cambiar de 50 a 100, de 8 a 4

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200
```

### 3. Detectar cuando todos los tiles se revelan ✨
```python
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
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    # ✅ NUEVO: Detectar si ganó
    if all(not h for h in hide):
        up()
        goto(0, 180)
        color('red')
        write('¡GANASTE!', align='center', font=('Arial', 40, 'bold'))
    
    update()
    ontimer(draw, 100)
```

### 4. Centrar números de un dígito 📍
```python
def draw():
    """Draw image and tiles."""
    # ... código anterior ...
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        number = tiles[mark]
        
        # ✅ NUEVO: Centrar según número de dígitos
        if number < 10:
            goto(x + 15, y + 10)  # Centrar números de 1 dígito
        else:
            goto(x + 2, y + 10)   # Números de 2 dígitos
        
        color('black')
        write(number, font=('Arial', 30, 'normal'))
    # ... resto del código ...
```

### 5. Usar letras en lugar de números 🔤
```python
from string import ascii_uppercase

# En lugar de números, usar letras
tiles = list(ascii_uppercase[:16]) * 2  # A-P repetidas
hide = [True] * 32

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    
    # La lógica de comparación funciona igual con letras
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
```

## Versión Completa: 4x4 con Contador

```python
from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(8)) * 2
state = {'mark': None, 'taps': 0, 'pairs': 0}
hide = [True] * 16

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    state['taps'] += 1
    spot = index(x, y)
    mark = state['mark']
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['pairs'] += 1

def draw():
    """Draw image and tiles."""
    clear()
    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 40, y + 40)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 40, 'normal'))
    
    # Mostrar estadísticas
    up()
    goto(-180, 180)
    color('black')
    write(f"Taps: {state['taps']} | Pares: {state['pairs']}/8", font=('Arial', 12, 'normal'))
    
    # Detectar victoria
    if state['pairs'] == 8:
        up()
        goto(0, 0)
        color('red')
        write('¡GANASTE!', align='center', font=('Arial', 50, 'bold'))
    
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
```

## Posibles Mejoras Avanzadas

- ⏱️ **Cronómetro** - Registrar tiempo por partida
- 📈 **Tabla de puntuaciones** - Guardar mejores tiempos
- 🎵 **Efectos de sonido** - Sonidos al revelar/emparejar
- 🎨 **Diferentes temas** - Colores, dificultades
- 🔐 **Sistema de dificultad** - Normal, Hard, Expert
- 💾 **Guardar progreso** - Reanudar partidas
- 🏆 **Logros** - Desbloquear con hitos
- 🖼️ **Imágenes en lugar de números** - Emparejar emojis o iconos

## Tips para Ganar

💡 **Consejos:**
1. **Memoriza patrones** - Recuerda dónde viste cada número
2. **Juega lentamente** - Tómate tu tiempo para pensar
3. **Concéntrate** - Reduce distracciones
4. **Práctica** - Cada juego te ayuda a memorizar mejor
5. **Busca secuencias** - Algunos números aparecen en zonas similares

## Licencia

Utiliza la librería `freegames` de [Giles Thomas](https://github.com/giles/freegames).

## Autor

Creado como práctica de programación de juegos con Turtle Graphics.

---

**¡A jugar!** 🧠 Ejecuta `python memory.py` y prueba tu memoria. ¿Cuántos taps necesitas para ganar?
