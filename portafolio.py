# Sugerencia y finalización de código
def sumarYmultiplicarPor10(primer_valor: float, segundo_valor: float) -> float:
    """Devuelve la suma de primer_valor y segundo_valor multiplicada por 10."""
    return (primer_valor + segundo_valor) * 10

def are_both_positive(first_value: int, second_value: int) -> bool:
    """Devuelve True solo si ambos valores son positivos."""
    return first_value > 0 and second_value > 0

# eliminar repetido
first_value = 1
second_value = 2
both_positive = are_both_positive(first_value, second_value)

# optimización / refactorización de código
def buscar_indice(items, objetivo):
    """
    Devuelve el índice de 'objetivo' en 'items' usando búsqueda lineal.
    Retorna -1 si no se encuentra.
    """
    for index, current in enumerate(items):
        if current == objetivo:
            return index
    return -1

# Nueva función: factorial
def factorial(n: int) -> int:
    """Devuelve el factorial de n (n!). Acepta solo enteros >= 0.
    Lanza TypeError si n no es int y ValueError si es negativo."""
    if not isinstance(n, int):
        raise TypeError("El factorial solo está definido para enteros.")
    if n < 0:
        raise ValueError("El factorial no está definido para enteros negativos.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Integración con pandas para crear un DataFrame
try:
    import pandas as pd  # type: ignore
except ImportError:  # pragma: no cover
    pd = None  # type: ignore

def crear_dataframe_factorial(max_n: int = 5):
    """Crea un DataFrame con n, factorial(n) y si n es positivo.
    Requiere pandas instalado."""
    if pd is None:
        raise ImportError("pandas no instalado. Instala con: pip install pandas")
    numeros = list(range(max_n + 1))
    data = {
        "n": numeros,
        "factorial": [factorial(n) for n in numeros],
        "es_positivo": [are_both_positive(n, 1) for n in numeros],
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    _example_factorial_5 = factorial(5)
    print(f"Factorial de 5 = {_example_factorial_5}")  # salida en consola
    if pd is not None:
        df = crear_dataframe_factorial(6)
        print("\nDataFrame factorial:")
        print(df)
    else:
        print("(Instala pandas para ver el DataFrame: pip install pandas)")

# code review