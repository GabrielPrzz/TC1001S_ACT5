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

## Caracteristicas Implementadas/Mejoradas


### 1. Visualiza el numero de taps! ✅
Para poder mejorar, implementamos el contador de taps, pudiendo ver si lo haces en menos intentos
```python
...
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
...

...
    # Mostrar contador de intentos
    up()
    goto(-195, 175)
    color('black')
    write(f'Intentos: {tap_count}', font=('Arial', 14, 'bold'))
...

```

### 2. Deteccion de todos los tableros descubiertos ✅
Se agrego a forma de win condition
```python
def all_revealed():
    """Return True if all tiles have been uncovered."""
    return not any(hide)
```

### 3. Centrado de texto en casillas ✅
Con fines de hacer mas estetico el display
```python

    # Escribir número en el centro
    if number is not None:
        up()
        goto(x + 25, y + 15)
        color('white')
        write(number, align='center', font=('Arial', 28, 'bold'))
        
```

### 4. Celdas de colores para facilitar la percepcion y la memoria ✅
```python
...
# 32 colores diferentes (necesitamos 32 pares para 64 casillas)
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 
          'pink', 'cyan', 'magenta', 'brown', 'gold', 'lime',
          'turquoise', 'salmon', 'khaki', 'coral', 'teal', 'navy',
          'olive', 'maroon', 'tomato', 'skyblue', 'springgreen', 'violet',
          'indigo', 'aquamarine', 'peachpuff', 'wheat', 'tan', 'plum', 'orchid', 'darkseagreen']

# Crear 32 pares diferentes: [(color, número), ...] * 2
base_tiles = [(colors[i], i + 1) for i in range(32)]
tiles = base_tiles + base_tiles  # 64 elementos totales
...

...
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
...
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
