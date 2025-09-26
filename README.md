# Alien Invasion

Alien Invasion es un juego arcade clásico desarrollado en Python utilizando la biblioteca Pygame. El objetivo es controlar una nave espacial, disparar a los alienígenas y evitar que lleguen a la parte inferior de la pantalla.

## Características

- Gráficos y animaciones con Pygame
- Control de la nave mediante teclado
- Disparo de proyectiles y colisiones con alienígenas
- Sistema de puntuación y récord
- Vidas limitadas y reinicio de partida
- Botón para jugar de nuevo
- Código organizado en módulos y orientado a objetos

## Requisitos

- Python 3.8 o superior
- Pygame 2.0 o superior

Instala las dependencias ejecutando:

```
pip install -r requirements.txt
```

## Estructura del proyecto

```
alien_invasion/
│
├── alien_invasion/        # Código fuente principal
│   ├── alien_invasion.py
│   ├── settings.py
│   ├── ship.py
│   ├── bullet.py
│   ├── alien.py
│   ├── game_stats.py
│   ├── button.py
│   ├── scoreboard.py
│   └── __pycache__/
│
├── images/                # Imágenes del juego (opcional)
├── requirements.txt
├── README.md
└── main.py                # Punto de entrada del juego
```

## Cómo jugar

1. Ejecuta el juego con:
   ```
   python main.py
   ```
2. Usa las flechas izquierda y derecha para mover la nave.
3. Pulsa la barra espaciadora para disparar.
4. Elimina todos los alienígenas para avanzar de nivel.
5. El juego termina si los alienígenas llegan abajo o te quedas sin vidas.

## Créditos

Desarrollado por Alex.  
Basado en el proyecto del libro "Python Crash Course" de Eric Matthes.

