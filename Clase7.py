def es_palindromo(palabra):
    """
    Determina si una palabra o frase es un palíndromo.
    Un palíndromo es una secuencia que se lee igual de izquierda a derecha que de derecha a izquierda,
    ignorando espacios y mayúsculas.

    Analogía:
    Imagina que tienes una cinta con letras escritas y quieres saber si, al girarla y leerla al revés,
    ves exactamente lo mismo. Primero limpias la cinta (eliminando espacios y mayúsculas), luego la comparas
    con su reflejo invertido. Si ambas lecturas son iguales, tienes un palíndromo.

    Parámetros:
        palabra (str): Palabra o frase a analizar.

    Returns:
        bool: True si la palabra/frase es palíndromo, False en caso contrario.
    """
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]