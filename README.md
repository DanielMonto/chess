# README

A continuación te explico como instalar y ejecutar `chess` de forma correcta en tu pc.

## Configurar el entorno virtual

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. Instala la herramienta `virtualenv` si aún no la tienes. Puedes instalarla utilizando pip:

    ```
    pip install virtualenv
    ```

3. Clona el repositorio del proyecto utilizando Git:

    ```
    git clone https://github.com/DanielMonto/chess.git
    ```
4. Cambia al directorio del proyecto clonado:

    ```
    cd chess/chess
    ```

5. Crea un entorno virtual dentro de este directorio:

    ```
    virtualenv venv
    ```

6. Activa el entorno virtual. Los comandos varían según tu sistema operativo:

    - En Windows:

        ```
        venv\Scripts\activate
        ```

    - En macOS y Linux:

        ```
        source venv/bin/activate
        ```

## Instalar Pygame

Una vez que el entorno virtual esté activado, puedes instalar Pygame utilizando pip:

    ```
    pip install pygame
    ```
## Ejecutar el proyecto

Ahora que tienes el entorno virtual configurado, Pygame instalado y el repositorio clonado, puedes ejecutar el proyecto. Asegúrate de estar en el directorio del proyecto (chess/chess) para ejecutarlo ejecuta:

    ```
    python main.py
    ```

¡Y eso es todo! Ahora deberías estar viendo y usando chess.


## Configuración del juego

El juego `chess` proporciona varias constantes que puedes ajustar para personalizar el comportamiento y la apariencia del juego. Aquí se detallan las constantes disponibles y sus posibles valores:

- `KNIGHT_SCORES`: Puntuaciones para los caballos en diferentes posiciones del tablero.
- `BISHOP_SCORES`: Puntuaciones para los alfiles en diferentes posiciones del tablero.
- `ROOK_SCORES`: Puntuaciones para las torres en diferentes posiciones del tablero.
- `QUEEN_SCORES`: Puntuaciones para las reinas en diferentes posiciones del tablero.
- `WHITE_P_SCORES`: Puntuaciones para los peones blancos en diferentes posiciones del tablero.
- `BLACK_P_SCORES`: Puntuaciones para los peones negros en diferentes posiciones del tablero.
- `KING_SCORES`: Puntuaciones para los reyes en diferentes posiciones del tablero.
- `PC_POSITIONS_SCORES`: Diccionario que asigna las puntuaciones según la pieza y su posición en el tablero.
- `WIDTH`, `HEIGHT`, `DIMENSION`, `SQ_SIZE`: Configuración del tamaño del tablero y las casillas.
- `MAX_FPS`: Cuadros por segundo máximos.
- `IMAGES`: Directorio de imágenes para las piezas del juego.
- `WHITE_PIECES`, `BLACK_PIECES`: Listas de las piezas blancas y negras.
- Coordenadas de los reyes blancos y negros (`WHITE_KING`, `BLACK_KING`).
- Colores para el tablero (`BRD_LIGHT_COLOR`, `BRD_DARK_COLOR`) y para las selecciones (`SQ_SELECTED_COLOR`, `SQ_SELECTED_MOVES_COLOR`, `LAST_MOVE_COLOR`).
- Configuraciones de enroque (`BKS_CASTLE`, `WKS_CASTLE`, `BQS_CASTLE`, `WQS_CASTLE`).
- `FRAMES_PER_SQPCANIMATION`: Cuadros por segundo para la animación de las piezas.
- `IA_DEPTH`: Profundidad de la búsqueda de la inteligencia artificial.
- `WHITE_HUMAN`, `BLACK_HUMAN`: Booleanos para especificar si los jugadores son humanos o controlados por la computadora.
- `PC_VALUES`: Valores asignados a cada tipo de pieza para la evaluación de la posición.

Puedes ajustar estas constantes según tus preferencias y requisitos del juego.