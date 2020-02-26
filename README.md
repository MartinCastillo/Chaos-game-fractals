# Uso
Al correr el archivo principal 

```bash
python python_chaos_game.py 
```

se empieza a generar el posible fractal con puntos pseudoaleatorios.

![captura1](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/captures/Captura1.PNG)
<br>

Cuantos más puntos se usen mejor será el resultado.
<br>

![captura1](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/captures/Captura2.PNG)
<br>

 Cuando está listo se guarda la imagen en la carpeta res y como nombre se le asignan ciertas configuraciones ajustables.
<br>

![captura1](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/captures/Captura3.PNG)
<br>
# Elementos importados

- cv2
- numpy
- math (ceil , sqrt)
- random (sample)
- os
 
# Funcionamiento

Se elige un punto de inicio y por cada iteración del programa elige uno de los vértices aleatoriamente (aunque se puede cambiar para que no reelija dos iguales seguidos), saca una fracción de la distacia entre el punto anterior y el vértice, para luego marcar el punto esa fración de distancia cerca del punto anterior al nuevo, en dirección al vértice (Si la fracción es 1/2, se marca el punto a mitad de camino).

[Más Detalles](https://en.wikipedia.org/wiki/Chaos_game "https://en.wikipedia.org/wiki/Chaos_game").


# Ejemplos

![captura1](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/res/puntos=10000;vertices=4;fraccion=0.6666666666666666;repetir_vertice=False.jpg)
![captura2](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/res/puntos=20000;vertices=3;fraccion=0.5;repetir_vertice=True.jpg)
![captura3](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/res/puntos=20000;vertices=4;fraccion=0.5;repetir_vertice=False.jpg)
![captura4](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/res/puntos=35000;vertices=5;fraccion=0.5;repetir_vertice=False.jpg)

