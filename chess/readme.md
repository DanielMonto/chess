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