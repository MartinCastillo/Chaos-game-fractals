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

Cuando está listo se guarda en la carpeta res, como nombre se le asignan ciertas configuraciones ajustables.
<br>

![captura1](https://raw.githubusercontent.com/MartinCastillo/Chaos-game-fractals-from_scratch/master/captures/Captura3.PNG)
<br>
# Elementos importados
<br>

1. cv2
2. numpy
3. math (ceil , sqrt)
4. random (sample)
5. os
 
# Funcionamiento
<br>
Se elige un punto de inicio y por cada iteración del programa elige uno de los vértices aleatoriamente (aunque se puede cambiar para que no reelija dos iguales seguidos), saca una fracción de la distacia entre el punto anterior y el vértice, para luego marcar el punto esa fración de distancia cerca del punto anterior al nuevo, en dirección al vértice (Si la fracción es 1/2, se marca el punto a mitad de camino).

[Más Detalles](https://en.wikipedia.org/wiki/Chaos_game "https://en.wikipedia.org/wiki/Chaos_game").

